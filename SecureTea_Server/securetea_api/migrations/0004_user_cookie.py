# Generated by Django 4.0.5 on 2022-06-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securetea_api', '0003_remove_user_loggedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cookie',
            field=models.CharField(default='', max_length=400),
        ),
    ]
