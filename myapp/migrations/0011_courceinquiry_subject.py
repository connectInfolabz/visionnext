# Generated by Django 5.0.4 on 2024-04-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_cource_courcescategories_courceinquiry_cource_cate'),
    ]

    operations = [
        migrations.AddField(
            model_name='courceinquiry',
            name='subject',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
