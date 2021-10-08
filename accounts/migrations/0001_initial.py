# Generated by Django 3.2.8 on 2021-10-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('password', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(max_length=60)),
                ('nickname', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
