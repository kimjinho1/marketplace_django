# Generated by Django 4.2.1 on 2023-05-24 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='create_by',
            new_name='created_by',
        ),
    ]
