# Generated by Django 3.1.3 on 2022-01-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapeasy', '0002_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]