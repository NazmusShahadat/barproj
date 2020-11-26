# Generated by Django 3.1.2 on 2020-10-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201021_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
    ]