# Generated by Django 3.2.16 on 2023-02-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='media')),
            ],
            options={
                'db_table': 'gallery',
            },
        ),
    ]
