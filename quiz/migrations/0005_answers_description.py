# Generated by Django 2.1.5 on 2019-01-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quiz_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
