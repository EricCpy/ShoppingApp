# Generated by Django 4.0.6 on 2022-07-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_customuser_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('SU', 'Superuser'), ('CS', 'Customer service'), ('CU', 'Customer')], default='CU', max_length=2),
        ),
    ]
