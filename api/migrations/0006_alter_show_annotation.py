# Generated by Django 4.2 on 2023-04-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_show_annotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='annotation',
            field=models.TextField(max_length=1000),
        ),
    ]
