from django import forms
from django.core.validators import RegexValidator

class ContactUSForm(forms.Form):
    full_name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=355,required=False)
    message=forms.CharField(max_length=3000)
    phone_number = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ),
        ]
    )


    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 10: 
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
