# Generated by Django 4.1.4 on 2022-12-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0003_post_video_id_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
