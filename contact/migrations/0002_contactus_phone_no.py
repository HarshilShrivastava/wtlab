# Generated by Django 3.2.2 on 2021-05-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='Phone_no',
            field=models.CharField(default='9039', max_length=13),
            preserve_default=False,
        ),
    ]