from django import forms

from UserApi.models import *


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = UserDetail.objects.filter(name=username)

        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return username


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserDetail
        fields = ('name', 'email', 'password')


class CodeForm(forms.ModelForm):
    class Meta:
        model = CodeDetail
        fields = '__all__'
