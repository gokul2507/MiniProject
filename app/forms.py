from django import forms

class create_form(forms.Form):
     d={}
     d["namef"] = forms.CharField(label="Name9", max_length=300)
     name=forms.CharField(label="Name ", max_length=300)