# Generated by Django 2.2.7 on 2020-05-14 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200514_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='bot_slots',
            field=models.CharField(default='none', max_length=500),
        ),
    ]