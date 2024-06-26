# Generated by Django 5.0.4 on 2024-04-10 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_serviceinquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('desc', models.TextField()),
                ('duration', models.CharField(max_length=60)),
                ('price', models.CharField(max_length=60)),
                ('totalStudents', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Cources')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='courcesCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ServiceCategories')),
                ('catename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='courceInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('courceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='cource',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.courcescategories'),
        ),
    ]
