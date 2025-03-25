from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # class Meta:
    #     model = User
    #     fields = ["username", "email", "password1", "password2"]

    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)


# class SignUpForm(forms.Form):
#     password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
#     confirm_password = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)
