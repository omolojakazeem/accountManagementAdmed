from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import forms, ModelForm

from .models import UserModel


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'school',
            'age',
            'gender')

    def save(self, commit=True):
        my_user = super(MyUserCreationForm, self).save(commit=False)
        my_user.school = self.cleaned_data['school']
        my_user.age = self.cleaned_data['age']
        my_user.gender = self.cleaned_data['gender']

        if commit:
            my_user.save()
        return my_user


class MyUserLogin(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1')
