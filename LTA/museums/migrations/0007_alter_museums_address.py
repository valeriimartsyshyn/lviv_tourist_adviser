# Generated by Django 3.2.9 on 2022-01-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museums', '0006_alter_museums_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museums',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]