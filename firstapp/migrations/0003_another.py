# Generated by Django 4.2.3 on 2023-09-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_rename_features_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Another',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
