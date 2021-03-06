# Generated by Django 4.0 on 2022-01-22 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vesti', '0003_izvor_vest_delete_vestosnovnestudije'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=200)),
                ('prezime', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('korisnik', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'profili',
            },
        ),
        migrations.CreateModel(
            name='Interesovanje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izvor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vesti.izvor')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='korisnici.profil')),
            ],
            options={
                'verbose_name_plural': 'interesovanja',
            },
        ),
    ]
