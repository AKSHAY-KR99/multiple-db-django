# Generated by Django 3.2.3 on 2022-03-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aqua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('content', models.CharField(max_length=50, verbose_name='content')),
                ('app_name', models.CharField(max_length=50, verbose_name='app_name')),
            ],
        ),
    ]
