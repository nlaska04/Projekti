# Generated by Django 5.1.4 on 2024-12-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_surname', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_comment', models.CharField(max_length=100)),
            ],
        ),
    ]
