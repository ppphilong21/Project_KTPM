# Generated by Django 3.2.8 on 2022-01-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20220127_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lop_tin_chi',
            name='type',
            field=models.CharField(choices=[('LT', 'LT'), ('TN', 'TN'), ('LT+BT', 'LT+BT')], default='LT', max_length=20, verbose_name='Loại lớp'),
        ),
    ]
