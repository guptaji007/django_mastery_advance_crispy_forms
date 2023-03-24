from django import forms
from .models import Candidate, SMOKER
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
    experience = forms.BooleanField(label='I have experience', required=False)
    message = forms.CharField(
        label='About you', min_length=50, max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder':'Talk a little about you', 'rows':3}
        )
    )
    # Method 1 (Gender)
    # GENDER = [('M', 'Male'), ('F', ('Female'))]
    # gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))

    class Meta:
        model = Candidate
        exclude = ['created_at', 'Situation']

        SALARY = (
            ('', ('Salary expectation (month)')),
            ('Between ($1000 and $2000)', ('Between ($1000 and $2000)')),
            ('Between ($2000 and $3000)', ('Between ($2000 and $3000)')),
            ('Between ($3000 and $4000)', ('Between ($3000 and $4000)')),
            ('Between ($4000 and $5000)', ('Between ($4000 and $5000)')),
        )
        # Method 2 Inside Meta Class for Gender
        GENDER = [('M', 'Male'), ('F', ('Female'))]

        # OUTSIDE WIDGETS
        widgets = {
            # Phone
            'phone': forms.TextInput(
                attrs={'style':'font-size: 13px', 
                       'placeholder': '(91) 99988-77766',
                       'data-mask': '(00) 00000-00000'
                }
            ),
            # Salary
            'salary': forms.Select(
                choices=SALARY,
                attrs={
                    'class':'form-control', # Bootstrap inside the forms.py
                }
            ), 
            'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check'}),
            'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check'}),
        }