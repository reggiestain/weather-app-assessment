# Generated by Django 2.2.16 on 2020-10-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NotesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesapp',
            name='content',
            field=models.TextField(),
        ),
    ]
