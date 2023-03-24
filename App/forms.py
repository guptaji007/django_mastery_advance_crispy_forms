from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Every Letter to LowerCase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
# Every Letter to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CandidateForm(forms.ModelForm):
    # FIRST NAME
    firstname = forms.CharField(
        label='First name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only Letters is Allowed!")],
        # Method 1 to replace native error message with custom message
        error_messages={'required': 'First Name cannot be Empty.'},
        # required=False,
        widget=forms.TextInput(attrs={
            'placeholder':'First name',
            'style': 'font-size: 13px; text-transform: capitalize'
        })
    )
    # LAST NAME
    lastname = forms.CharField(
        label='Last name', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only Letters is Allowed!")],
        # required=False,
        widget=forms.TextInput(attrs={
            'placeholder':'Last name',
            'style': 'font-size: 13px; text-transform: capitalize'
        })
    )
    # JOB CODE (UPPERCASE FUNCTION)
    job = Uppercase(
        label='Job Code', min_length=5, max_length=5,
        # required=False,
        widget=forms.TextInput(attrs={
            'placeholder':'Example: FR-22',
            'style': 'font-size: 13px; text-transform: uppercase'
        })
    )
    # Email (LOWERCASE FUNCTION)
    email = Lowercase(
        label='Email Address', min_length=8, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message="Put a valid email address!")],
        # required=False,
        widget=forms.TextInput(attrs={
            'placeholder':'Email Address',
            'style': 'font-size: 13px; text-transform: lowercase'
        })
    )
    # Method 1 to validate age
    # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))

    # Method 2 to validate age
    age = forms.CharField(
        label='Your age', min_length=2, max_length=3,
        validators=[RegexValidator(r'^[0-9]*$', 
        message="Only numbers is Allowed!")],
        # Method 1 to replace native error message with custom message
        error_messages={'required': 'Age field cannot be Empty.'},
        # required=False,
        widget=forms.TextInput(attrs={
            'placeholder':'Age', 
            'style': 'font-size: 13px'
        })
    )
    # EXPERIENCE
    experience = forms.BooleanField(label='I have experience', required=False)
    # MESSAGE
    message = forms.CharField(
        label='About you', min_length=50, max_length=1000,
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder':'Talk a little about you', 
            'rows':3,
            'style': 'font-size: 13px'
            })
    )
    # FILE (UPLOAD)
    file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(attrs={
                'style': 'font-size: 13px'
            })
    )

    # Method 1 (Gender)
    # GENDER = [('M', 'Male'), ('F', ('Female'))]
    # gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))

    class Meta:
        model = Candidate
        exclude = ['created_at', 'Situation']

        # Labels Control
        # labels = {
            # 'phone':'You Phone',
            # 'personality':'Your personality',
            # 'salary':'Choose a salary',
            # 'gender':'Your gender',
            # 'smoker':'Do you smoker?',
        # }

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
                    'style': 'font-size: 13px'
                }
            ), 
            'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check'}),
            'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check'}),
            'personality': forms.Select(attrs={'style': 'font-size: 13px'})
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # =========== CONTROL PANEL | INDIVIDUAL INPUTS ===========#
        # 1) INPUT REQUIRED
        # self.fields['experience'].required = True

        # 2) INPUT DISABLED
        # self.fields['experience'].disabled = False
        
        # 3) INPUT READONLY
        # self.fields['email'].widget.attrs.update({'readonly':'readonly'})

        # 4) SELECT OPTION
        self.fields['personality'].choices = [('', 'Select a personality'),] + list(self.fields['personality'].choices)[1:]
            
        # 5) WIDGETS CONTROL (INSIDE / OUTSIDE)
        # self.fields['phone'].widget.attrs.update({'style':'font-size: 18px', 'placeholder': 'No Phone', 'data-mask': '(00) 00-00'})
        
        # 6) ERROR MESSAGES
        # Method 2 to replace native error message with custom message
        # self.fields['firstname'].error_messages.update({
        #     'required': 'Django Mastery Channel'
        # })

        # =========== ADVANCED CONTROL PANEL | MULTIPLE INPUTS BY 'LOOP FOR' IN [ARRAY] ===========#
        # 1) READONLY
        # readonly = ['firstname', 'lastname', 'job', 'email', 'age', 'phone']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # 2) DISABLED
        # disabled = ['personality', 'salary', 'gender', 'smoker', 'experience']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'

        # 3) ERROR MESSAGES
        # Method 3 to replace native error message with custom message
        # error_messages = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality', 'salary', 'gender', 'smoker']
        # for field in error_messages:
        #     self.fields[field].error_messages.update({'required': 'Django Mastery Channel'})

        # 4) FONT SIZE
        # font_size = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality', 'salary']
        # for field in font_size:
        #     self.fields[field].widget.attrs.update({'style': 'font-size: 18px'})

    # ---------- END of SUPER FUNCTION -----------------------

    # FUNCTION TO PREVENT DUPLICATED ENTRIES
    # Method 1 using For Loop
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     for obj in Candidate.objects.all():
    #         if obj.email == email:
    #             raise forms.ValidationError('Denied! ' + email + ' is already registered.')
    #     return email
    
    # Method 2 using if statement with filter queryset
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Candidate.objects.filter(email = email).exists():
            raise forms.ValidationError('Denied! {} is already registered.'.format(email))
        return email