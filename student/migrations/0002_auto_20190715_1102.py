# Generated by Django 2.1.2 on 2019-07-15 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='student_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_number',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
