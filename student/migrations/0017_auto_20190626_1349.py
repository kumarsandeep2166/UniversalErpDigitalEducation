# Generated by Django 2.1.2 on 2019-06-26 08:19

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20190626_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_certificate',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='clc',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='conduct_certificate',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='migration',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='signature',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='thumb',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth',
            field=models.ImageField(upload_to=student.models.PathAndRename('documents/2019/06/26')),
        ),
    ]
