# Generated by Django 4.0.5 on 2022-06-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_profile_coverletter_alter_profile_cv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
