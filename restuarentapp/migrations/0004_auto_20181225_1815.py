# Generated by Django 2.0.5 on 2018-12-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarentapp', '0003_menuitem_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='photo',
            field=models.ImageField(blank=True, upload_to='item_image/'),
        ),
    ]
