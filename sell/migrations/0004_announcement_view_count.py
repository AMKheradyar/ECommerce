# Generated by Django 4.1.4 on 2023-01-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_alter_announcement_owner_delete_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
