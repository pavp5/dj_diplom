# Generated by Django 5.0.2 on 2024-04-02 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
    ]
