from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    # customized password
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password',
        
    }))
    

    # fields from model Account
    class Meta:
        model=Account
        fields=['first_name','last_name','email','phone_number','password']

    
    # styling all the fields with the same class
         
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter first name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter last name'
        self.fields['email'].widget.attrs['placeholder']='Email Address'
        self.fields['phone_number'].widget.attrs['placeholder']='Phone number'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control '
    

    def clean(self):
        cleaned_data=super(RegistrationForm, self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "password doesn't match"
            )