from django import forms
from .models import Register,Login
# Reordering Form and View



class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
