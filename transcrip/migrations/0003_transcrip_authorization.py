# Generated by Django 3.2.12 on 2023-04-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcrip', '0002_auto_20210619_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcrip',
            name='authorization',
            field=models.FileField(default=0, upload_to='pdf_files'),
            preserve_default=False,
        ),
    ]
