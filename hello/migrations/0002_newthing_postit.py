# Generated by Django 2.2.2 on 2019-06-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newthing',
            name='postit',
            field=models.IntegerField(default=0),
        ),
    ]
