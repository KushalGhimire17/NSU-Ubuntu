from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

province_choices = [
        ("1", "Province No. 1"), 
        ("2", "Province No. 2"), 
        ("3", "Bagmati Pradesh"), 
        ("4", "Gandaki Pradesh"), 
        ("5", "Province No. 5"),
        ("6", "Karnali Pradesh"),
        ("7", "Sudurpashchim Pradesh"),
    ]
class UserRegisterForm(UserCreationForm):
    mobile_number = forms.IntegerField()
    province = forms.ChoiceField(choices=province_choices)
    district = forms.CharField(max_length=20)
    campus = forms.CharField(max_length=200)
    current_role = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100, label='Permanent Address')


    class Meta:
        model = User
        fields = ['username', 'mobile_number', 'province', 'district', 'campus', 'current_role', 'address']
