# Generated by Django 2.2.7 on 2021-05-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_rename_name_notice_signatory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='signatory',
            field=models.CharField(max_length=40),
        ),
    ]
