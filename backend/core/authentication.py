from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import NGO
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class NGOAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Use the default JWTAuthentication first
        jwt_auth = JWTAuthentication()
        validated_token = None

        # Try to validate the JWT token
        try:
            validated_token = jwt_auth.get_validated_token(request)
        except AuthenticationFailed:
            return None  # Not a valid JWT token, proceed with other authentication methods if needed

        # Extract the user type (this assumes you're encoding user type in the token claims)
        user_type = validated_token.get('user_type')  # Assuming 'user_type' is part of your JWT claims

        if user_type == 0:  # Assuming 0 indicates an NGO
            ngo = NGO.objects.get(id=validated_token['user_id'])
            if ngo:
                return (ngo, validated_token)  # Return the NGO instance

        return None  # No valid NGO found

    def authenticate_header(self, request):
        return 'Bearer'  # Return the authentication scheme
