# Generated by Django 4.2.1 on 2023-06-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=10)),
                ('coefficient', models.IntegerField()),
            ],
        ),
    ]