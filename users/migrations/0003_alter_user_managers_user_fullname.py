# Generated by Django 5.0.6 on 2024-06-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='Albert Iradukunda', max_length=255, verbose_name='Full Name'),
            preserve_default=False,
        ),
    ]
