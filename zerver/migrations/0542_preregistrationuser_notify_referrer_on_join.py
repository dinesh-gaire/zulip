# Generated by Django 5.0.6 on 2024-06-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0541_alter_realmauditlog_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="preregistrationuser",
            name="notify_referrer_on_join",
            field=models.BooleanField(default=True),
        ),
    ]