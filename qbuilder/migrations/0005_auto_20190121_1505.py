# Generated by Django 2.1.4 on 2019-01-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbuilder', '0004_auto_20190121_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ques_create',
            name='importance',
            field=models.CharField(max_length=6),
        ),
    ]
