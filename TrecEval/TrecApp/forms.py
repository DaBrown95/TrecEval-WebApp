from django import forms
from TrecApp.models import Run, Researcher, Task

class ResearcherForm(forms.form):
    name = forms.CharField(max_length=128, help_text="Please enter your name")
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
        fields = ('name','url','display_name','organization')

  
