# Generated by Django 2.1.3 on 2018-11-16 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20181114_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(default=' ', upload_to='books/'),
            preserve_default=False,
        ),
    ]
