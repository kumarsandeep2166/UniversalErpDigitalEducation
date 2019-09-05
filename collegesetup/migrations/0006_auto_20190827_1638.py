# Generated by Django 2.1.7 on 2019-08-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegesetup', '0005_basesetup_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basesetup',
            name='affiliated_body',
        ),
        migrations.AddField(
            model_name='basesetup',
            name='affiliated_body',
            field=models.ManyToManyField(blank=True, to='collegesetup.AffiliatedTo'),
        ),
        migrations.RemoveField(
            model_name='basesetup',
            name='approval',
        ),
        migrations.AddField(
            model_name='basesetup',
            name='approval',
            field=models.ManyToManyField(blank=True, to='collegesetup.Approval'),
        ),
        migrations.RemoveField(
            model_name='basesetup',
            name='approved_body',
        ),
        migrations.AddField(
            model_name='basesetup',
            name='approved_body',
            field=models.ManyToManyField(blank=True, to='collegesetup.Accredited_Body'),
        ),
        migrations.AlterField(
            model_name='basesetup',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]