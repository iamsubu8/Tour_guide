# Generated by Django 4.0.3 on 2022-04-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0002_tourpackage_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200)),
                ('place_pic', models.ImageField(null=True, upload_to='tourImages')),
            ],
        ),
    ]
