# Generated by Django 3.0.5 on 2020-04-14 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('num_pages', models.IntegerField(default=0)),
                ('date_published', models.DateField()),
            ],
        ),
    ]
