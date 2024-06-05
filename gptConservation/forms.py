from django import forms
from .models import Conversation

class UserForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['user_input']

 