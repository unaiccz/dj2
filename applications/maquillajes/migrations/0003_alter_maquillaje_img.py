# Generated by Django 4.1.5 on 2023-02-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maquillajes", "0002_alter_maquillaje_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maquillaje",
            name="img",
            field=models.ImageField(upload_to="media/", verbose_name="imagen"),
        ),
    ]
