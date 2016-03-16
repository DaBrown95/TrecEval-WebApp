from django import forms
from TrecApp.models import Run, run_type, query_type, feedback_type
from TrecApp.models import run_type
from django_enumfield import enum

class RunForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter name of your run.")
    run_type = forms.TypedChoiceField(choices=run_type.choices(), coerce=int)
    query_type = forms.TypedChoiceField(choices=query_type.choices(), coerce=int)
    feedback_type = forms.TypedChoiceField(choices=feedback_type.choices(), coerce=int)
    description = forms.CharField(widget=forms.Textarea)
    runfile = forms.FileField(label='Select a run to upload',help_text='max. 42 megabytes')

    MAP = forms.DecimalField(widget=forms.HiddenInput())
    p10 = forms.DecimalField(widget=forms.HiddenInput())
    p20 = forms.DecimalField(widget=forms.HiddenInput())
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Run
        fields = ('runfile',)
