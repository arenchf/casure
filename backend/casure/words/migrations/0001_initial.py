# Generated by Django 3.2.11 on 2022-04-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('translation', models.CharField(max_length=512)),
                ('points', models.IntegerField(default=0)),
                ('example_sentence', models.TextField()),
                ('last_training', models.DateTimeField(verbose_name='date last trained')),
            ],
        ),
    ]
