# Generated by Django 3.2.3 on 2021-06-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210610_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='img',
            field=models.CharField(default='https://static.wikia.nocookie.net/mario/images/c/cd/Mario_Cap.png/revision/latest?cb=20180310022043', max_length=500),
        ),
    ]