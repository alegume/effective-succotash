# Generated by Django 3.2.4 on 2021-07-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.BigIntegerField(null=True),
        ),
    ]