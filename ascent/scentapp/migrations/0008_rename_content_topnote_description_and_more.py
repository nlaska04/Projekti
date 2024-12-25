# Generated by Django 5.1.4 on 2024-12-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scentapp', '0007_delete_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topnote',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='topnote',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='topnote',
            name='image',
        ),
        migrations.AlterField(
            model_name='topnote',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]