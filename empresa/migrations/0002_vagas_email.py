# Generated by Django 4.1.3 on 2022-11-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
