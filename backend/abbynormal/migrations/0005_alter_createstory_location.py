# Generated by Django 4.0.4 on 2022-04-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abbynormal', '0004_createstory_story_title_delete_storylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstory',
            name='location',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
