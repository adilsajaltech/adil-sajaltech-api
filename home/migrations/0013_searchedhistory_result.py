# Generated by Django 5.0 on 2023-12-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_searchedhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchedhistory',
            name='result',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]