from django import forms
from . models import Data, Predictions
from django.core.validators import RegexValidator

# EVERY LETTER TO UPPER CASE


class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class DataForm(forms.ModelForm):
    # VALIDATIONS
    software_id = Uppercase(
        label='Software Id', min_length=4, max_length=50,
        # required=False,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        widget=forms.TextInput(
            attrs={'placeholder': 'Software Id'})
    )

    branchCount = forms.CharField(
        label='Branch Count', min_length=1, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 1 Max: 30'})
    )

    hashvalue = forms.CharField(
        # required=False,
        label='Hash Value',
        widget=forms.TextInput(attrs={'placeholder': 'Hash-Value'})
    )

    class Meta:
        model = Data
        fields = ['software_id', 'license_key',
                  "hashvalue", 'branchCount', "predictions"]
        # exclude = ("tested_at", "predictions")

        widgets = {
            'license_key': forms.TextInput(
                attrs={'style': 'font-size:16px',
                       'placeholder': 'XXXXX-XXXXX-XXXXX-XXXXX',
                       'data-mask': '00000 - 00000 - 00000 - 00000'
                       }
            ),
        }


class PredictionsForm(forms.ModelForm):
    softwarename = forms.CharField(
        label='Software Name', min_length=4, max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Software Name'})
    )

    branchCount = forms.CharField(
        label='Branch Key', min_length=1, max_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 1 Max: 30'})
    )

    Hashvalue = forms.CharField(
        label='Hash Value', min_length=2, max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'KHYTGFRDEW'})
    )

    licensekey = forms.CharField(
        label='License Key', min_length=5, max_length=23,
        widget=forms.TextInput(attrs={'placeholder': 'XXXXX-XXXXX-XXXXX-XXXXX'})
    )

    class Meta:
        model = Predictions
        fields = ['softwarename','licensekey', 'Hashvalue', 'branchCount', "Predictions"]

    # SUPPER FUNCTION
    # def __init__(self, *args, **kwargs):
    #     super(DataForm, self).__init__(*args, **kwargs)
