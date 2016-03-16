from django import forms
from TrecApp.models import Run, run_type, query_type, feedback_type
from django_enumfield import enum

class RunForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter name of your run")
    run_type = forms.TypedChoiceField(choices=run_type.choices(), coerce=int)
    query_type = forms.TypedChoiceField(choices=query_type.choices(), coerce=int)
    feedback_type = forms.TypedChoiceField(choices=feedback_type.choices(), coerce=int)
    description = forms.CharField(widget=forms.Textarea)

    runfile = forms.FileField(label='runUpload',help_text='Upload your run file')

    MAP = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    p10 = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    p20 = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    # An inline class to provide additional information on the form.

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Run
        fields = ('runfile','name','description','run_type','query_type','feedback_type','MAP','p10','p20')
        exclude = ('researcher','task',)
