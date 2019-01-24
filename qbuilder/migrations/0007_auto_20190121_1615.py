# Generated by Django 2.1.4 on 2019-01-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbuilder', '0006_auto_20190121_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules_id', models.CharField(max_length=8)),
                ('static_id', models.CharField(max_length=8)),
                ('parent_id', models.CharField(max_length=8)),
                ('correct_id', models.CharField(max_length=8)),
                ('wrong_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='ques_rules',
        ),
    ]
