# Generated by Django 3.0.6 on 2020-06-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
