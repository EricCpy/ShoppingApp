# Generated by Django 4.0.5 on 2022-07-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('SU', 'superuser'), ('CS', 'customer service'), ('CU', 'customer')], default='CU', max_length=2),
        ),
    ]
