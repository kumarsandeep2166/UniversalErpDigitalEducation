# Generated by Django 2.1.2 on 2019-06-27 06:23

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20190626_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.ImageField(upload_to=course.models.PathAndRename('syllabus/2019/06/27')),
        ),
    ]
