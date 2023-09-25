from django import forms
from .models import Speaking, Writing, PracticeW, PracticeS

class SpeakingForm(forms.ModelForm):
    class Meta:
        model = Speaking
        fields = ['type','problem', 'solution']

class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ['type','problem', 'solution']
class WritingPracticeForm(forms.ModelForm):
    class Meta:
        model = PracticeW
        fields = ['problem', 'solution']

class SpeakingPracticeForm(forms.ModelForm):
    class Meta:
        model = PracticeS
        fields = ['problem', 'solution']

