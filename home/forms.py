from django import forms

class ContactUSForm(forms.Form):
    full_name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=355,required=False)
    message=forms.CharField(max_length=3000)


    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 10: 
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
