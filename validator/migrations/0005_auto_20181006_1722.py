# Generated by Django 2.1 on 2018-10-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0004_validationrun_name_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=80)),
                ('help_text', models.CharField(max_length=150)),
            ],
        ),
    ]
