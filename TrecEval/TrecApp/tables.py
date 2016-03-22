import django_tables2 as tables
from django_tables2.utils import A
from TrecApp.models import Run, Researcher, Task


class RunTable(tables.Table):
    name = tables.Column(verbose_name='Name')
    researcher = tables.Column(verbose_name='Researcher')
    task = tables.Column(verbose_name='Task')
    runfile = tables.Column()
    description = tables.Column(verbose_name='Description')
    run_type = tables.Column(verbose_name='Run Type')
    query_type = tables.Column(verbose_name='Query Type')
    feedback_type = tables.Column(verbose_name='Feedback Type')
    MAP = tables.Column()
    p10 = tables.Column(verbose_name='P10')
    p20 = tables.Column(verbose_name='P20')
    organization = tables.Column(verbose_name='Organization')

    class Meta:
        model = Run

class TaskTable(tables.Table):
    title = tables.LinkColumn('task',verbose_name='Title',args =[A('slug')])
    year = tables.Column(verbose_name='Year')
    number = tables.Column(verbose_name='Number of Runs')

    class Meta:
        model = Task
        exclude = ('ID','track','task_url','description','judgement_file','slug')

class ResearcherTable(tables.Table):
    display_name = tables.LinkColumn('researcher', verbose_name='Name', args=[A('slug')])
    organization = tables.Column(verbose_name='Organizations')
    numberOfRuns = tables.Column(verbose_name='No. Runs')

    class Meta:
        model = Researcher
        exclude = ('slug','picture','user','url')
