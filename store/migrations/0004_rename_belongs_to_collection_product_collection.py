# Generated by Django 4.0.2 on 2022-02-06 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_store_custo_first_n_8f83e0_idx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='belongs_to_collection',
            new_name='collection',
        ),
    ]
