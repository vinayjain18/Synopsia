# Generated by Django 4.0.2 on 2022-02-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_new_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
