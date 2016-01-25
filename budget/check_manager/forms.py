from django import forms
from check_manager.models import Check
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = '__all__'
        exclude = []