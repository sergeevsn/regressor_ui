from django import forms

class UploadFileForm(forms.Form):
    file1 = forms.FileField(label='Upload Features File:', widget=forms.FileInput(attrs={'class': 'form-control mt-3'}))
    file2 = forms.FileField(label='Upload Target File:', widget=forms.FileInput(attrs={'class': 'form-control mt-3'}))