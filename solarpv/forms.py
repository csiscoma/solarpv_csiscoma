from django import forms

class SolarPVForm(forms.Form):
    client = forms.CharField(label='Client', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
    product = forms.CharField(label='Product', max_length=100)
    teststandard = forms.CharField(label='Test Standard', max_length=100)
    certificate = forms.CharField(label='Certificate', max_length=100)