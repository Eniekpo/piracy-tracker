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
        label='Branch Count', min_length=2, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: -0.8 Max: 2.5'})
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
    software_name = forms.CharField(
        label='Software Name', min_length=4, max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Software Name'})
    )

    branchCount = forms.CharField(
        label='Branch Key', min_length=2, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 0.1 Max: 2.5'})
    )

    total_Op = forms.CharField(
        label='Hash Value', min_length=2, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 0.1 Max: 2.5'})
    )

    total_Opnd = forms.CharField(
        label='License Key', min_length=2, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 0.1 Max: 2.5'})
    )

    unique_Opnd = forms.CharField(
        label='Unique Opnd', min_length=2, max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 0.1 Max: 2.5'})
    )

    class Meta:
        model = Predictions
        fields = ['software_name','unique_Opnd', 'total_Op',
                  'total_Opnd', 'branchCount', "Predictions"]

    # SUPPER FUNCTION
    # def __init__(self, *args, **kwargs):
    #     super(DataForm, self).__init__(*args, **kwargs)
