# Generated by Django 4.0.5 on 2022-06-09 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('matricule', models.CharField(max_length=15)),
                ('complain', models.CharField(max_length=100)),
                ('prove', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
