# Generated by Django 2.2 on 2022-05-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220517_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
