# Generated by Django 3.2.12 on 2022-02-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0002_Add_Role_Employee_LeaveType_Leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_description',
            field=models.TextField(blank=True),
        ),
    ]
