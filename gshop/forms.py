from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Иия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone_regex = RegexValidator(regex="\+375[0-9]{9}", message="Введите номер телефона в формате +375000000000")
    phone_number = forms.CharField(label='Номер телефона', validators=[phone_regex],
                                    max_length=13, widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

