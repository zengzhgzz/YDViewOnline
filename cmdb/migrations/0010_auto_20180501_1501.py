# Generated by Django 2.0.4 on 2018-05-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0009_auto_20180501_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinfo',
            name='user',
            field=models.CharField(default='admin', max_length=255, verbose_name='用户'),
            preserve_default=False,
        ),
    ]
