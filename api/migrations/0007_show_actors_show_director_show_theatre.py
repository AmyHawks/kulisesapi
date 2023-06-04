# Generated by Django 4.2 on 2023-04-20 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_show_annotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='actors',
            field=models.ManyToManyField(to='api.actor'),
        ),
        migrations.AddField(
            model_name='show',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.director'),
        ),
        migrations.AddField(
            model_name='show',
            name='theatre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.theatre'),
        ),
    ]