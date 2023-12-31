# Generated by Django 4.2.6 on 2023-11-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(max_length=126)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=64)),
                ('contra', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('dni', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
