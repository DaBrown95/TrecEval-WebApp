import django_tables2 as tables
import unicodedata
from django.utils.safestring import mark_safe
from django_tables2.utils import A
from TrecApp.models import Run, Researcher, Task

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name

    def __init__(self, classname=None, *args, **kwargs):
        self.classname=classname
        super(CheckBoxColumnWithName, self).__init__(*args, **kwargs)

    #creates html for checkbox
    def render(self, value):
        value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
        return mark_safe("<input type='checkbox' class ='" + self.classname +  "' value='" + value + "'/>"  )

class DivWrappedLinkColumn(tables.LinkColumn):
    def __init__(self, classname=None, *args, **kwargs):
        self.classname=classname
        super(DivWrappedLinkColumn, self).__init__(*args, **kwargs)

    #creates html for table cell with a url in it
    def render(self, value):
        print value
        return mark_safe("<a href='/trecapp/run/" + str(value) + "'>" + str(value) + "</a>")  


class DivWrappedColumn(tables.Column):
    def __init__(self, classname=None, *args, **kwargs):
        self.classname=classname
        super(DivWrappedColumn, self).__init__(*args, **kwargs)

    #creates html for table cell
    def render(self, value):
        return mark_safe("<div class='" + self.classname + "' >" + str(value)+"</div>")

    
class RunTable(tables.Table):
    name = DivWrappedLinkColumn(classname = 'name_column', verbose_name='Name', args=[A('slug')])
    researcher = DivWrappedColumn(classname = 'researcher_column',verbose_name='Researcher')
    task = DivWrappedColumn(classname = 'task_column',verbose_name='Task')
    runfile = DivWrappedColumn(classname = 'run_column')
    description = DivWrappedColumn(classname = 'description_column',verbose_name='Description')
    run_type = DivWrappedColumn(classname = 'runtype_column',verbose_name='Run Type')
    query_type = DivWrappedColumn(classname = 'querytype_column',verbose_name='Query Type')
    feedback_type = DivWrappedColumn(classname = 'feedbacktype_column',verbose_name='Feedback Type')
    MAP = DivWrappedColumn(classname = 'map_column')
    p10 = DivWrappedColumn(classname = 'p10_column',verbose_name='P10')
    p20 = DivWrappedColumn(classname = 'p20_column',verbose_name='P20')
    organization = DivWrappedColumn(classname = 'organization_column',verbose_name='Organization')
    checkBox = CheckBoxColumnWithName(classname = 'checkbox_column',verbose_name="Create Graph?")

    class Meta:
        model = Run
        attrs = {'class':'RobbTable'}
        



class TaskTable(tables.Table):
    title = tables.LinkColumn('task', verbose_name='Title', args=[A('slug')])
    year = tables.Column(verbose_name='Year')
    number = tables.Column(verbose_name='Number of Runs')

    class Meta:
        model = Task
        exclude = ('ID', 'track', 'task_url', 'description', 'judgement_file', 'slug')


class ResearcherTable(tables.Table):
    display_name = tables.LinkColumn('researcher', verbose_name='Name', args=[A('slug')])
    organization = tables.Column(verbose_name='Organizations')
    numberOfRuns = tables.Column(verbose_name='No. Runs')

    class Meta:
        model = Researcher
        exclude = ('slug', 'picture', 'user', 'url')

