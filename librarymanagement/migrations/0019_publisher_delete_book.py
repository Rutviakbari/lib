# Generated by Django 4.0.2 on 2022-03-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanagement', '0018_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='publisher',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=50, primary_key=b'I01\n', serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
