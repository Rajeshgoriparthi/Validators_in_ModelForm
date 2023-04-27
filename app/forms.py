from django import forms
from django.core import validators

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('First Charector Should not be a')

def check_for_len(value):
    if len(value)<3:
        raise forms.ValidationError('length morthan the 6 charectors')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=30,validators=[check_for_a,check_for_len])
    age=forms.IntegerField(validators=[validators.MinValueValidator(18)])
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=50,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data.get('email')
        r=self.cleaned_data.get('re_enter_email')
        if e!=r:
            raise forms.ValidationError('Email Not matched')


    def clean_botcatcher(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise forms.ValidationError('data is not enterd')
