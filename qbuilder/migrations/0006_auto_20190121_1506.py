# Generated by Django 2.1.4 on 2019-01-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbuilder', '0005_auto_20190121_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ques_create',
            name='complexity',
            field=models.TextField(max_length=6),
        ),
    ]
