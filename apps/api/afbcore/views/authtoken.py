from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from ..serializers.user import UserSerializer

# NOTE: The passwordless "token/code" is only ever set to is_active=False
# in two places (both in drfpasswordless/utils.py):
#
#   1. authenticate_by_token() -- not called within passwordless
#   2. validate_token_age() -- called by validate_token() in passwordless
#
# That's why magic links stay valid even after they're used. They stay
# valid and (currently) can be used N times until they expire.
# See: PASSWORDLESS_TOKEN_EXPIRE_TIME in settings.py.


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = "UserSerializer"

    def post(self, request, version=None):
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
