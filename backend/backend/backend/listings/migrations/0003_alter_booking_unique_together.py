# Generated by Django 5.2.3 on 2025-07-03 09:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_booking'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('user', 'listing')},
        ),
    ]
