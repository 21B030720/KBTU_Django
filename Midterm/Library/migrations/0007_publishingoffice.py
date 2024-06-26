# Generated by Django 5.0.3 on 2024-03-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_client_email_client_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(default='default@example.com', max_length=254)),
                ('address', models.CharField(default='default@example.com', max_length=255)),
            ],
            options={
                'db_table': 'publishing_office',
            },
        ),
    ]
