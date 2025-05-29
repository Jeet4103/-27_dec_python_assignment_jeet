from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor
    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'Enter your First Name'}),
    )
    
    last_name = forms.CharField(    
        required=True,
        widget=forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Enter your Last Name'}),
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Enter your Email'}),
    )
    
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Choose a Username'}),
    )
    
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Create a Password'}),
    )
    
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'id': 'confirm-password', 'placeholder': 'Confirm your Password'}),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        # Remove default labels
        for field in self.fields:
            self.fields[field].label = ""

        # Set help texts to empty to prevent Django from adding default hints
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None



class DoctorEditForm(forms.ModelForm):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'name', 
            'placeholder': 'Enter full name'
        }),
    )
    
    specialty = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'specialty', 
            'placeholder': 'Enter specialty'
        }),
    )

    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'phone_number', 
            'placeholder': 'Enter phone number'
        }),
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'id': 'email', 
            'placeholder': 'Enter email'
        }),
    )

    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'address', 
            'placeholder': 'Enter address'
        }),
    )

    fees = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'id': 'fees', 
            'placeholder': 'Enter consultation fees'
        }),
    )

    discription = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'id': 'description', 
            'placeholder': 'Write a short description',
            'rows': 4
        }),
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'id': 'image'
        }),
    )

    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone_number', 'email', 'address', 'fees', 'discription', 'image']

        wigets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 0.75rem;'}),
                'specialty': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 0.75rem;'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 0.75rem;'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 0.75rem;'}),
                'address': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 0.75rem;'}),
                'fees': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 0.75rem;'}),
                'discription': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%; padding: 0.75rem;'}),
                'image': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'style': 'width: 100%;'})
        }

    def __init__(self, *args, **kwargs):
        super(DoctorEditForm, self).__init__(*args, **kwargs)

        # Remove default labels
        for field in self.fields:
            self.fields[field].label = ""

        # Remove help texts
        for field in self.fields:
            self.fields[field].help_text = None
