from  django import forms


#this is for signup form

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))