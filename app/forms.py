from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-light rounded-3 border-0 py-3',
            'placeholder': 'Full Name',
            'required': True
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control bg-light rounded-3 border-0 py-3',
            'placeholder': 'Email Address',
            'required': True
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-light rounded-3 border-0 py-3',
            'placeholder': 'Phone Number',
            'required': True
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control bg-light rounded-3 border-0 py-3',
            'rows': 4,
            'placeholder': 'Message / What do you need help with?',
            'required': True
        })
    )
