# Generated by Django 4.1.1 on 2023-01-21 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_parent'),
        ('listings', '0008_listing_posted_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.detail')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.amenity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
