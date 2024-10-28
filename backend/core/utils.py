# import uuid
# from venv import logger
# from django.utils import timezone
# from datetime import timedelta
# from .models import NGOToken

# # utils.py
# def generate_ngo_token(ngo):
#     token_str = str(uuid.uuid4())  # Generate a unique token string
#     token = NGOToken.objects.create(
#         ngo=ngo,
#         token=token_str,
#         expires_at=timezone.now() + timedelta(days=2)
#     )
#     return token_str


# # utils.py
# def validate_ngo_token(token):
#     try:
#         ngo_token = NGOToken.objects.get(token=token)
#         if ngo_token.is_expired():
#             return False
#         return ngo_token.ngo
#     except NGOToken.DoesNotExist:
#         return False