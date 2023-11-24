from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# from afbcore.serializers import UserSerializer


class VueformValidatorsView(APIView):
    permission_classes = (AllowAny,)
    # serializer_class = UserSerializer

    @action(detail=False, methods=["post"])
    def check_unique_email(self, request):
        """
        Confirm the email address is unique.
        """
        # serializer = self.get_serializer(request.user, context={"request": request})

        # return Response(serializer.data)
