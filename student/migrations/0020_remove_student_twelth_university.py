# Generated by Django 2.1.2 on 2019-06-26 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_auto_20190626_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='twelth_university',
        ),
    ]
