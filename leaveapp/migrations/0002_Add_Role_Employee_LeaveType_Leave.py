# Generated by Django 3.2.12 on 2022-02-25 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Full names'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Leave'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_title',
            field=models.CharField(max_length=100, verbose_name='Role'),
        ),
    ]
