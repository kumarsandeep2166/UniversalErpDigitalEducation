# Generated by Django 2.1.2 on 2019-07-15 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanagement', '0011_auto_20190715_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='feesmanagementsetting',
            name='stream',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Stream'),
            preserve_default=False,
        ),
    ]
