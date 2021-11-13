from django import forms

from mainapp.models import LoadFiles


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
