# Generated by Django 3.1.7 on 2021-04-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classdetail', '0008_classdetailcs4142_classdetailcs4344_classdetailcs45'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdetailcs3132',
            name='subteach',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AlterField(
            model_name='classdetailcs3334',
            name='subteach',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AlterField(
            model_name='classdetailcs4142',
            name='classgroup',
            field=models.CharField(default='4142', max_length=4),
        ),
        migrations.AlterField(
            model_name='classdetailcs4142',
            name='subteach',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AlterField(
            model_name='classdetailcs4344',
            name='classgroup',
            field=models.CharField(default='4344', max_length=4),
        ),
        migrations.AlterField(
            model_name='classdetailcs4344',
            name='subteach',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AlterField(
            model_name='classdetailcs45',
            name='classgroup',
            field=models.CharField(default='45', max_length=4),
        ),
        migrations.AlterField(
            model_name='classdetailcs45',
            name='subteach',
            field=models.CharField(default='N/A', max_length=60),
        ),
    ]
