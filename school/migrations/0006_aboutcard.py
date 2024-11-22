# Generated by Django 5.1 on 2024-08-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_partner_alter_result_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225, verbose_name='Card name')),
                ('name_uz', models.CharField(max_length=225, null=True, verbose_name='Card name')),
                ('name_en', models.CharField(max_length=225, null=True, verbose_name='Card name')),
                ('name_ru', models.CharField(max_length=225, null=True, verbose_name='Card name')),
                ('icon', models.ImageField(max_length=255, upload_to='', verbose_name='Card icon')),
                ('description', models.TextField(max_length=255, verbose_name='Card description')),
                ('description_uz', models.TextField(max_length=255, null=True, verbose_name='Card description')),
                ('description_en', models.TextField(max_length=255, null=True, verbose_name='Card description')),
                ('description_ru', models.TextField(max_length=255, null=True, verbose_name='Card description')),
            ],
            options={
                'verbose_name': 'About page card',
                'verbose_name_plural': 'About page cards',
            },
        ),
    ]