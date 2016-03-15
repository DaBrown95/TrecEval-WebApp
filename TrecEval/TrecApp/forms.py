from django import forms
from TrecApp.models import Run

class RunForm(forms.Form):
    runfile = forms.FileField(
        label='Select a run to upload',
        help_text='max. 42 megabytes'
    )
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Run
        fields = ('runfile',)

  
