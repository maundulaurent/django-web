# Generated by Django 4.2 on 2024-04-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buniwa', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='author',
        ),
        migrations.AddField(
            model_name='blogs',
            name='author_image',
            field=models.ImageField(default=2, upload_to='author_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='author_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
