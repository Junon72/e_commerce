# Generated by Django 3.0.5 on 2020-05-20 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_date',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='created_date',
        ),
    ]
