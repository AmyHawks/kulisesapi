# Generated by Django 4.2 on 2023-06-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_show_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]
