# Generated by Django 2.2.5 on 2019-11-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='md',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
