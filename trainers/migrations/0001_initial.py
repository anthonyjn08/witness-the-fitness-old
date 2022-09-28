# Generated by Django 3.2 on 2022-09-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_email', models.EmailField(max_length=254)),
                ('trainer_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('trainer_bio', models.TextField()),
                ('trainer_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
