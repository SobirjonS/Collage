# Generated by Django 5.1 on 2024-08-26 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='About title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='About title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='About title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='About title')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, verbose_name='About slug')),
                ('image', models.ImageField(upload_to='about/', verbose_name='About image')),
                ('description', models.TextField(verbose_name='About description')),
                ('description_uz', models.TextField(null=True, verbose_name='About description')),
                ('description_en', models.TextField(null=True, verbose_name='About description')),
                ('description_ru', models.TextField(null=True, verbose_name='About description')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
    ]