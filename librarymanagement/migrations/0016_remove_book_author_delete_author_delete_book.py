# Generated by Django 4.0.2 on 2022-03-14 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanagement', '0015_delete_fruit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]