# Generated by Django 3.2.10 on 2022-01-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('text', models.TextField(max_length=400)),
                ('name', models.TextField(max_length=100)),
            ],
        ),
    ]
