# Generated by Django 3.1.2 on 2020-10-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_delete_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=10)),
            ],
        ),
    ]