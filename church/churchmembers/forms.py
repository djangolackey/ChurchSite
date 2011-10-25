from django.forms import ModelForm
from churchmembers.models import Family

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ('name', 'photo', 'address', 'address2', 'city', 'state', 'zip', 'phone1', 'phone2', 'email', 'website',)