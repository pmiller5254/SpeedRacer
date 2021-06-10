# Generated by Django 3.2.3 on 2021-06-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_record_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='release_date',
        ),
        migrations.AddField(
            model_name='game',
            name='release_year',
            field=models.CharField(default=1995, max_length=20),
            preserve_default=False,
        ),
    ]