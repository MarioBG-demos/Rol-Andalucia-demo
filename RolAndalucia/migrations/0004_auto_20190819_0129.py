# Generated by Django 2.1.7 on 2019-08-18 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0003_auto_20190818_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='castTime',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='description',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='materialComponent',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='materialRequirements',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='range',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='save',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='somaticComponent',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='verbalComponent',
        ),
    ]
