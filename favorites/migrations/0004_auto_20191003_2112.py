# Generated by Django 2.2.5 on 2019-10-04 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0003_auto_20191003_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoritelines',
            old_name='favorite_lines',
            new_name='favoriteLines',
        ),
    ]