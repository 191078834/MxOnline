# Generated by Django 2.0.1 on 2019-06-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20190603_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='reacher/%Y%m', verbose_name='头像'),
        ),
    ]
