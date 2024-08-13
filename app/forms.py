from django import forms

from app.models import *

class StudentMF(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    
    botcatcher=forms.CharField(widget=forms.HiddenInput(),required=False)

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
        



        