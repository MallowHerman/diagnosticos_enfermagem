# Generated by Django 4.1.3 on 2022-12-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanda', '0006_alter_diagnoses_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
