from django import forms
from . models import Data
from django.core.validators import RegexValidator


class DataForm(forms.ModelForm):
    # VALIDATIONS
    software_name = forms.CharField(
        label='Software Name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
                                   message='Only letter is allowed !')],
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Software Name'})
    )

    uniq_Opnd = forms.CharField(
        label='Uniq_Opnd', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]+$',
                                   message='Only numbers is allowed !')],
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 0.8 Max: 7.9'})
    )

    total_Op = forms.CharField(
        label='Total_Op', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]+$',
                                   message='Only numbers is allowed !')],
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 2.0 Max: 4.0'})
    )

    total_Opnd = forms.CharField(
        label='Total_Opnd', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]+$',
                                   message='Only numbers is allowed !')],
        widget=forms.TextInput(attrs={'placeholder': 'MIN: 1.0 Max: 6.9'})
    )

    branchCount = forms.CharField(
        label='Branch Count', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]+$',
                                   message='Only numbers is allowed !')],
        widget=forms.TextInput(attrs={'placeholder': 'MIN: -0.8 Max: 2.5'})
    )

    class Meta:
        model = Data
        # fields = ['software_name', 'uniq_Opnd', 'total_Op', 'total_Opnd', 'branchCount']
        exclude = ("date", "predictions")
