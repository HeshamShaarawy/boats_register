from django.forms import ModelForm
from .models import Gear


class GearForm(ModelForm):
    class Meta:
        model = Gear
        fields = ['item', 'quantity']

