from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import User, NGO, Donation
from .serializers import UserSerializer, NGOSerializer, DonationSerializer
from .authentication import NGOAuthentication
import logging

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication, NGOAuthentication]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            logger.info(f"Updating user with data: {request.data}")
            response = super().update(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error updating user: {e}")
            return Response({'error': 'User update failed'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            logger.info(f"Fetching users with data: {request.data}")
            response = super().list(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching users: {e}")
            return Response({'error': 'Fetching users failed'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            logger.info(f"Fetching user with id: {kwargs['pk']}")
            response = super().retrieve(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching user: {e}")
            return Response({'error': 'Fetching user failed'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")


class NGOViewSet(viewsets.ModelViewSet):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer
    authentication_classes = [JWTAuthentication, NGOAuthentication]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        elif hasattr(self.request, 'ngo') and self.request.ngo is not None:
            return []  # NGO authenticated
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        try:
            logger.info(f"Updating NGO with data: {request.data}")
            response = super().update(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error updating NGO: {e}")
            return Response({'error': 'NGO update failed'}, status=status.HTTP_400_BAD_REQUEST)

    def get_ngos(self, request, *args, **kwargs):
        try:
            logger.info(f"Fetching NGOs with data: {request.data}")
            response = super().list(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching NGOs: {e}")
            return Response({'error': 'Fetching NGOs failed'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    authentication_classes = [JWTAuthentication, NGOAuthentication]

    def get_permissions(self):
        if hasattr(self.request, 'ngo') and self.request.ngo is not None:
            self.permission_classes = [IsAuthenticated]
        elif hasattr(self.request, 'is_ngo_authenticated') and self.request.is_ngo_authenticated:
            return []
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        if hasattr(request, 'ngo') and request.ngo is not None:
            logger.info(f"Creating donation for NGO: {request.ngo}")
        else:
            logger.info(f"Creating donation for User: {request.user}")

        try:
            response = super().create(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating donation: {e}")
            return Response({'error': 'Donation creation failed'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def destroy(self, request, *args, **kwargs):
            raise MethodNotAllowed("DELETE")
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    logger.info(f"Login attempt for email: {email}")

    if not email or not password:
        logger.error("Email or password missing.")
        return Response({'error': 'Email and password required'}, status=status.HTTP_400_BAD_REQUEST)

    # Check User model
    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        logger.info(f"User authenticated: {user.email}")
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': 1
        }, status=status.HTTP_200_OK)

    # Check NGO model
    ngo = NGO.objects.filter(email=email).first()
    if ngo and check_password(password, ngo.password):  # Ensure 'password' is stored in a hashed format
        logger.info(f"NGO authenticated: {ngo.email}")

        # Manually create a refresh token
        refresh = RefreshToken()
        refresh['user_id'] = str(ngo.ngo_id)  # Use the NGO's ID
        refresh['user_type'] = 0  # Assuming 0 indicates NGO

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': 0
        }, status=status.HTTP_200_OK)

    logger.error("Invalid credentials provided.")
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
