from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm

from authapp.models import UserProfile, Status


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'


class RegisterForm(UserCreationForm, forms.ModelForm):
    status = forms.CharField(label='Кто вы?', widget=forms.Select(choices=Status.choices))

    class Meta:
        model = UserProfile
        fields = (
            'username',
            'first_name',
            'last_name',
            'status',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''


class ChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'
            item.help_text = ''
            if name == 'password':
                item.widget = forms.HiddenInput()


class ChangePassword(PasswordChangeForm):
    class Meta:
        model = UserProfile
        fields = 'password'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'

    def get_form(self, form_class):
        return form_class(self.request.user, **self.get_form_kwargs())
