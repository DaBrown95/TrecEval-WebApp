import django_tables2 as tables
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
