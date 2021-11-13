from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
            'email'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''

    # def save(self, commit=True):
    #     user = super().save(commit=commit)  # call native method
    #     UserProfile.objects.create(user=user)
    #     return user
