# Generated by Django 3.0.1 on 2020-09-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tender', '0014_auto_20200906_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Tender_Image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
