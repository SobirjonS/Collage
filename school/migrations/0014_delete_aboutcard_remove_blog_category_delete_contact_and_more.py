# Generated by Django 5.1 on 2024-11-27 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_delete_partner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutCard',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
    ]
