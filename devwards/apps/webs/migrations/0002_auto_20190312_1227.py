# Generated by Django 2.1.7 on 2019-03-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='websites'),
        ),
    ]