import logging

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from afbcore.models import User

logger = logging.getLogger(__name__)


class VueformUniqueValidatorView(APIView):
    """
    This class is used to validate the uniqueness of a user field.
    """

    permission_classes = (AllowAny,)

    def post(self, request, formate=None):
        """
        This method is used to validate the uniqueness of a user field.

        @see https://vueform.com/docs/validating-elements#rule-unique

        e.g. Request payload from Vueform:

            {
                "params": {},
                "name": "email",
                "value": "greg@notadiagnosis.com"
            }

        """
        logger.info("VueformUniqueValidatorView.post")
        logger.info(request.data)

        field_name = request.data.get("name", None)
        field_value = request.data.get("value", None)

        is_unique = self.is_a_truly_unique(field_name=field_name, value=field_value)

        if is_unique:
            return Response("true", status=status.HTTP_200_OK)
        else:
            # Possibly a 409 Conflict would be more appropriate. Vueform
            # may have specific handling for 409s.
            return Response("false", status=status.HTTP_200_OK)

    def is_a_truly_unique(self, field_name, value):
        """
        This method is used to check the given email address against the database.

        """
        logger.info("VueformValidatorsView.is_a_truly_unique")

        is_unique = False

        if field_name == "email":
            is_unique = User.objects.is_a_truly_unique(
                field_name=field_name, value=value
            )

        else:
            msg = f"Not able to validate '{field_name}' just yet"
            logger.warning(msg)
            raise NotImplementedError(msg)

        return is_unique
