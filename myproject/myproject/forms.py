from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class FetchDataForm(forms.Form):
    api_url = forms.URLField()
    link_url = forms.URLField()
