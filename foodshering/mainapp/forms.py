from django import forms

from mainapp.models import LoadFiles, Group


class LoadFileForm(forms.ModelForm):
    class Meta:
        model = LoadFiles
        fields = (
            'file',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'
            item.help_text = ''


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'name',
            'users_volonter',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'
            item.help_text = ''
