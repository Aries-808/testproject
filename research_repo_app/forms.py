from django import forms
from .models import Thesis, ResearchPaper, ResearchData



class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
class ResearchDataForm(forms.ModelForm):
    class Meta:
        model = ResearchData
        fields = ['title', 'data_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'data_file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }