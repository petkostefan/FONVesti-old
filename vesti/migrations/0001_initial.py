# Generated by Django 4.0 on 2022-01-01 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VestOsnovneStudije',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=255)),
                ('opis', models.TextField()),
                ('vreme', models.DateTimeField()),
                ('link', models.CharField(max_length=255)),
                ('img_link', models.CharField(max_length=255)),
            ],
        ),
    ]