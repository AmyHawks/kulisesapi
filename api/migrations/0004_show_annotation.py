# Generated by Django 4.2 on 2023-04-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_actor_director_theatre'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='annotation',
            field=models.CharField(default='Lorem ipsum dolor sit amet', max_length=1000),
        ),
    ]
