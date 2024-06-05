# Generated by Django 5.0.6 on 2024-06-05 21:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gptConservation', '0002_alter_question_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_input', models.TextField()),
                ('bot_response', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
