from django import forms
from . models import Data
from django.core.validators import RegexValidator

# EVERY LETTER TO UPPER CASE


class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class DataForm(forms.ModelForm):
    # VALIDATIONS
    software_id = Uppercase(
        label='Software Id', min_length=4, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        widget=forms.TextInput(
            attrs={'placeholder': 'Software Id'})
    )

    uniq_Opnd = forms.CharField(
        label='Uniq_Opnd', min_length=2, max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 0.8 Max: 7.9'})
    )

    total_Op = forms.CharField(
        label='Branch Count', min_length=2, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 2.0 Max: 4.0'})
    )

    total_Opnd = forms.CharField(
        label='Total_Opnd', min_length=2, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 1.0 Max: 6.9'})
    )

    hashvalue = forms.CharField(
        label='Hash Value',
        widget=forms.TextInput(attrs={'placeholder': 'hash'})
    )

    class Meta:
        model = Data
        fields = ['software_id', 'uniq_Opnd', 'total_Op',
                  'total_Opnd', 'license_key', "hashvalue", "predictions"]
        # exclude = ("tested_at", "predictions")

        widgets = {
            'license_key': forms.TextInput(
                attrs={'style': 'font-size:16px',
                       'placeholder': 'XXXXX-XXXXX-XXXXX-XXXXX',
                       'data-mask': '00000 - 00000 - 00000 - 00000'
                       }
            ),
        }

    # SUPPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
