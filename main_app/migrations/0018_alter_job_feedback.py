# Generated by Django 4.0.5 on 2022-06-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='feedback',
            field=models.TextField(blank=True, default='', max_length=250),
        ),
    ]
