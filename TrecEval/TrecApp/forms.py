from django import forms
from django.contrib.auth.models import User
from django_enumfield import enum
from TrecApp.models import Run, Researcher, Task, run_type, query_type, feedback_type

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ResearcherForm(forms.ModelForm):
    display_name = forms.CharField(max_length=128, help_text="Please enter a display name")
    organization = forms.CharField(max_length=128, help_text="Please enter your organization")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of your web-page. Not required",required = False)

    def clean(self):        #tidy up url
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Researcher
        fields = ('url','display_name','organization')


class RunForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter name of your run")
    run_type = forms.TypedChoiceField(choices=run_type.choices(), coerce=int)
    query_type = forms.TypedChoiceField(choices=query_type.choices(), coerce=int)
    feedback_type = forms.TypedChoiceField(choices=feedback_type.choices(), coerce=int)
    description = forms.CharField(widget=forms.Textarea)
    task = forms.ModelChoiceField(queryset=Task.objects.all().order_by('title'))
    runfile = forms.FileField(label='runUpload',help_text='Upload your run file')

    MAP = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    p10 = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    p20 = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    # An inline class to provide additional information on the form.

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Run
        fields = ('runfile','name','description','run_type','query_type','feedback_type','MAP','p10','p20','task',)
        exclude = ('researcher',)
