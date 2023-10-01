# Generated by Django 4.2.4 on 2023-08-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demotemplateapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='pictures')),
                ('image', models.ImageField(upload_to='pictures')),
                ('head', models.TextField()),
                ('para', models.TextField()),
            ],
        ),
    ]