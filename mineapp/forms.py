from django import forms
from .models import CreateUser
class SignIn(forms.ModelForm):
    class Meta:
        model = CreateUser
        fields = ['name', 'password', 'email']
    password = forms.CharField(widget=forms.PasswordInput())
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if CreateUser.objects.filter(name=name).exists():
            raise forms.ValidationError('Пользователь с таким name уже существует.')
        return name
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CreateUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email