# Generated by Django 4.2.6 on 2023-10-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_advocate_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
