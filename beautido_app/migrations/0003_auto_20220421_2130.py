# Generated by Django 2.2 on 2022-04-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautido_app', '0002_auto_20220329_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girl',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]