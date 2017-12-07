from django import forms

from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactInfo
        fields = [
            'first_name',
            'last_name',
            'email',
            'verify_email',
            'message'
        ]