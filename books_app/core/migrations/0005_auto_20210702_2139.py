# Generated by Django 3.1.7 on 2021-07-02 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210702_2055'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('user', 'title')},
        ),
    ]