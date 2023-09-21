

from django.forms import ModelForm

from afbcore.models import Client


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "email",
            "address",
            "phone_number",
            "status"
        ]
