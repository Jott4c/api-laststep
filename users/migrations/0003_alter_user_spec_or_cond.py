# Generated by Django 4.1.4 on 2022-12-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_address_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="spec_or_cond",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
