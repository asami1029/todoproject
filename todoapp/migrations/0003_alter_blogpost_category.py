# Generated by Django 4.2 on 2025-01-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('ニュース', 'ニュース')], max_length=50, verbose_name='カテゴリ'),
        ),
    ]
