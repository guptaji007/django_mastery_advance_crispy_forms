from django import forms
from .models import Candidate
from django.core.validators import RegexValidator

# Every Letter to LowerCase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
# Every Letter to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CandidateForm(forms.ModelForm):
    # VALIDATIONS
    firstname = forms.CharField(
        label='First name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only Letters is Allowed!")],
        # required=False,
        widget=forms.TextInput(attrs={'placeholder':'First name'})
    )
    lastname = forms.CharField(
        label='Last name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only Letters is Allowed!")],
        # required=False,
        widget=forms.TextInput(attrs={'placeholder':'Last name'})
    )
    # Job Code Always in Uppercase
    job = Uppercase(
        label='Job Code', min_length=5, max_length=5,
        # required=False,
        widget=forms.TextInput(attrs={'placeholder':'Example: FR-22'})
    )
    # Email Always in Lowercase
    email = Lowercase(
        label='Email Address', min_length=8, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message="Put a valid email address!")],
        # required=False,
        widget=forms.TextInput(attrs={'placeholder':'Email Address'})
    )
    # Method 1 to validate age
    # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))

    # Method 2 to validate age
    age = forms.CharField(
        label='Your age', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]*$', 
        message="Only numbers is Allowed!")],
        # required=False,
        widget=forms.TextInput(attrs={'placeholder':'Age'})
    )
    message = forms.CharField(
        label='About you', min_length=50, max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder':'Talk a little about you', 'rows':5}
        )
    )

    class Meta:
        model = Candidate
        exclude = ['created_at', 'Situation']
        
        # Outside Widget
        widgets = {
            'phone': forms.TextInput(
                attrs={'style':'font-size: 13px', 
                       'placeholder': '(91) 99988-77766',
                       'data-mask': '(00) 00000-00000'
                }
            )
        }