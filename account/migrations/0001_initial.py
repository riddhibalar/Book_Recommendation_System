# Generated by Django 3.0.2 on 2020-03-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('Interest', models.CharField(max_length=150)),
            ],
        ),
    ]
