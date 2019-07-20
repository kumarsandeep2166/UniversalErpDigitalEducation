# Generated by Django 2.1.2 on 2019-07-17 06:12

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190716_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree_marksheet',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_address',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_birth_certificate',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_clc',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_conduct_certificate',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_degree',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_migration',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_pic',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_signature',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_tenth',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_thumb',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_twelth',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_marksheet',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
        migrations.AlterField(
            model_name='student',
            name='tewlth_marksheet',
            field=models.ImageField(blank=True, upload_to=student.models.PathAndRename('documents/2019/07/17')),
        ),
    ]