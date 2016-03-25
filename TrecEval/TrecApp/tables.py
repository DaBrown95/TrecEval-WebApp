import django_tables2 as tables
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django_tables2.utils import A

from TrecApp.models import Run, Researcher, Task


class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class NameLinkColumn(tables.LinkColumn):
    def __init__(self, classname=None, *args, **kwargs):
        self.classname = classname
        super(NameLinkColumn, self).__init__(*args, **kwargs)

    # creates html for table cell with a url in it
    def render(self, value):
        slugvalue = slugify(value)
        return mark_safe("<a href='/trecapp/run/" + str(slugvalue) + "' class='name_col'>" + str(value) + "</a>")


class ResearcherNameLinkColumn(tables.LinkColumn):
    def __init__(self, classname=None, *args, **kwargs):
        self.classname = classname
        super(ResearcherNameLinkColumn, self).__init__(*args, **kwargs)

    # creates html for table cell with a url in it
    def render(self, value):
        slugvalue = slugify(value)
        return mark_safe("<a href='/trecapp/researcher/" + str(slugvalue) + "' class='name_col'>" + str(value) + "</a>")


class TaskNameLinkColumn(tables.LinkColumn):
    def __init__(self, classname=None, *args, **kwargs):
        self.classname = classname
        super(TaskNameLinkColumn, self).__init__(*args, **kwargs)

    # creates html for table cell with a url in it
    def render(self, value):
        slugvalue = slugify(value)
        return mark_safe("<a href='/trecapp/tasks/" + str(slugvalue) + "' class='name_col'>" + str(value) + "</a>")


class DivWrappedColumn(tables.Column):
    def __init__(self, classname=None, *args, **kwargs):
        self.classname = classname
        super(DivWrappedColumn, self).__init__(*args, **kwargs)

    # creates html for table cell
    def render(self, value):
        return mark_safe("<div class='" + self.classname + "' >" + str(value) + "</div>")


class RunTable(tables.Table):
    name = NameLinkColumn('run', verbose_name='Name', args=[A('slug')])
    researcher = DivWrappedColumn(classname='standard_col', verbose_name='Researcher')
    task = DivWrappedColumn(classname='standard_col', verbose_name='Task')
    runfile = DivWrappedColumn(classname='standard_col')
    description = DivWrappedColumn(classname='standard_col', verbose_name='Description')
    run_type = DivWrappedColumn(classname='standard_col', verbose_name='Run Type')
    query_type = DivWrappedColumn(classname='standard_col', verbose_name='Query Type')
    feedback_type = DivWrappedColumn(classname='standard_col', verbose_name='Feedback')
    MAP = DivWrappedColumn(classname='standard_col')
    p10 = DivWrappedColumn(classname='standard_col', verbose_name='P10')
    p20 = DivWrappedColumn(classname='standard_col', verbose_name='P20')
    date = DivWrappedColumn(classname='standard_col', verbose_name='Date')
    organization = DivWrappedColumn(classname='standard_col', verbose_name='Organization')
    checkBox = CheckBoxColumnWithName(verbose_name="Create Graph?")

    class Meta:
        model = Run
        attrs = {'class': 'RobbTable'}


class TaskTable(tables.Table):
    title = TaskNameLinkColumn('task', verbose_name='Title', args=[A('slug')])
    year = DivWrappedColumn(verbose_name='Year', classname='standard_col')
    number = DivWrappedColumn(verbose_name='Number of Runs', classname='standard_col')

    class Meta:
        model = Task
        exclude = ('ID', 'track', 'task_url', 'description', 'judgement_file', 'slug')


class ResearcherTable(tables.Table):
    display_name = ResearcherNameLinkColumn('researcher', verbose_name='Name', args=[A('slug')])
    organization = DivWrappedColumn(verbose_name='Organizations', classname='standard_col')
    numberOfRuns = DivWrappedColumn(verbose_name='No. Runs', classname='standard_col')

    class Meta:
        model = Researcher
        exclude = ('slug', 'picture', 'user', 'url')
