# Generated by Django 4.0.5 on 2022-06-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securetea_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='loggedin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
