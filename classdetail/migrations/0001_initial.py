# Generated by Django 3.1 on 2020-09-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subcode', models.CharField(max_length=10)),
                ('url', models.URLField(blank=True)),
                ('meetid', models.CharField(max_length=11)),
                ('password', models.TextField()),
            ],
        ),
    ]
