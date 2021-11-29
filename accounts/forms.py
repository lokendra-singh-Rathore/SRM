from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import *
from django import forms

class studentloginform(ModelForm):
    class Meta:
        model=Studentlogin
        fields='__all__'



class OrderForm(ModelForm):
	class Meta:
		model = Topic
		fields = '__all__'


class FeeForm(ModelForm,forms.DateInput):
    class Meta:
        model = Fee
        fields = '__all__'
        widgets = {
            'upcoming_Due_Date': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'})

        }


class StudentForm(ModelForm,forms.DateInput):
    class Meta:
        model=Student
        fields='__all__'
        widgets = {
            'Student_name': forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'Father_name': forms.TextInput(attrs={'placeholder': 'Father Name'}),
            'Mother_name': forms.TextInput(attrs={'placeholder': 'Mother Name'}),
            'School_name': forms.TextInput(attrs={'placeholder': 'School Name'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'Address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'Father_occupation': forms.TextInput(attrs={'placeholder': 'Father Occupation'}),
            'Mother_occupation': forms.TextInput(attrs={'placeholder': 'Mother Occupation'}),
            'Father_Contact_no': forms.TextInput(attrs={'placeholder': 'Father Contact no'}),
            'Mother_Contact_no': forms.TextInput(attrs={'placeholder': 'Mother Contact no'}),
            'Class': forms.TextInput(attrs={'placeholder': 'Class'}),
            'DOB': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'})
        }
class demoform(ModelForm):
    class Meta:
        model=bookdemo
        fields='__all__'
        widgets = {
            'your_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'student_name': forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'school_name': forms.TextInput(attrs={'placeholder': 'School Name'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Contact'}),
            'msg': forms.TextInput(attrs={'placeholder': 'Other Details'}),
        }


class contactform(ModelForm):
    class Meta:
        model=contact
        fields='__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'msg': forms.TextInput(attrs={'placeholder': 'Give Us More  Details'}),
        }