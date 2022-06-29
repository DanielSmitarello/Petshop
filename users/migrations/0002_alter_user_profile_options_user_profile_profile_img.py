# Generated by Django 4.0.4 on 2022-06-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_profile',
            options={'verbose_name': 'Perfil de Usuario', 'verbose_name_plural': 'Perfiles de Usuario'},
        ),
        migrations.AddField(
            model_name='user_profile',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='profile_image'),
        ),
    ]
