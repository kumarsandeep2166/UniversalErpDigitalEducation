# Generated by Django 2.1.2 on 2019-07-18 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeplan', '0004_feesplantype_default_installment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesplantype',
            name='fees_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Feestype'),
        ),
    ]
