# Generated by Django 4.0.5 on 2022-09-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twitte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('like', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
