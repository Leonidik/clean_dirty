# Generated by Django 4.0.5 on 2022-11-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs_work', '0002_rename_userslog_authorlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorlog',
            name='author_ip',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]