# Generated by Django 4.0 on 2021-12-10 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_is_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='classs',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
