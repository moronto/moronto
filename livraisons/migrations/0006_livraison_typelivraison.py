# Generated by Django 5.1.5 on 2025-03-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraisons', '0005_remove_livraison_condtrans_remove_livraison_mattrans_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livraison',
            name='typeLivraison',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
