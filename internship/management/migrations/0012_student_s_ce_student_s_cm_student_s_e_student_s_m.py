# Generated by Django 4.1.1 on 2022-11-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_alter_student_s_address_alter_student_s_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='S_ce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='S_cm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='S_e',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='S_m',
            field=models.BooleanField(default=False),
        ),
    ]
