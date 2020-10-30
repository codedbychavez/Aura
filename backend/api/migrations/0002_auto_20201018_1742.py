# Generated by Django 3.0.5 on 2020-10-18 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_tag', models.CharField(default='', max_length=100)),
                ('project_desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='va',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
            preserve_default=False,
        ),
    ]
