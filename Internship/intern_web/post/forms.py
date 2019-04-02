from django import forms
from .models import  Apply


# this form is created for posting intern in post.html


# class PostForm(forms.ModelForm):
#     Posting_title = forms.CharField(widget=forms.TextInput(
#                                             attrs={'class': 'form-control', 'placeholder': 'Project manager'}
#                                             ))
#     Location = forms.CharField(widget=forms.TextInput(
#                                             attrs={'class': 'form-control', 'placeholder': 'Dhaka'}
#                                             ))
#     job_type = forms.CharField(widget=forms.TextInput(
#                                             attrs={'class': 'form-control', 'placeholder': 'Full Time'}
#                                             ))
#     deadline = forms.CharField(widget=forms.TextInput(
#                                             attrs={'class': 'form-control', 'placeholder': 'October 2, 2018'}
#                                             ))
#     Internship_discription = forms.CharField(widget=forms.Textarea(
#                                             attrs={'class': 'form-control', 'placeholder': 'Describe..'}
#                                             ))
#
#     class Meta:
#         model = Post
#         fields = {
#             'Posting_title',
#             'Internship_discription',
#             'Location',
#             'job_type',
#             'deadline'
#         }
#

# this form is created for applying intern in apply.html


class applyForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'jobaer hossain'}
                                ))
    Expected_salery = forms.IntegerField(widget=forms.NumberInput(
                                attrs={'class': 'form-control', 'placeholder': '12000'}
                                ))
    address = forms.CharField(widget=forms.Textarea(
                                attrs={'class': 'form-control', 'placeholder': 'house/road'}
                                ))
    nationality = forms.CharField(widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Bangladeshi'}
                                ))
    email = forms.EmailField(widget=forms.EmailInput(
                                attrs={'class': 'form-control', 'placeholder': 'jh@gmail.com'}
                                ))
    contact = forms.CharField(widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': '0162...'}
                                ))
    # birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1970, 2000)))
    birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Apply
        fields = {
            'full_name',
            'Expected_salery',
            'nationality',
            'email',
            'contact',
            'address',
            'birth'
        }