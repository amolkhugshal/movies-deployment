# Generated by Django 2.2.5 on 2020-01-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.TextField(),
        ),
    ]
