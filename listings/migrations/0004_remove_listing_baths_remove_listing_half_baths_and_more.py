# Generated by Django 4.1.1 on 2022-12-24 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_detail_listing_city_listing_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='baths',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='half_baths',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='rooms',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='size',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='year_built',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='listingfloorplan',
            name='floor_2d',
        ),
        migrations.RemoveField(
            model_name='listingfloorplan',
            name='floor_3d',
        ),
        migrations.AddField(
            model_name='listing',
            name='area',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='listing',
            name='country',
            field=models.CharField(default='Serbia', max_length=150),
        ),
        migrations.AddField(
            model_name='listingfloorplan',
            name='floor_plan',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.CreateModel(
            name='ListingCharacteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('structure', models.DecimalField(decimal_places=1, max_digits=4)),
                ('year_built', models.IntegerField(null=True)),
                ('floor', models.IntegerField(null=True)),
                ('total_floors', models.IntegerField(null=True)),
                ('bedrooms', models.DecimalField(decimal_places=1, max_digits=4)),
                ('baths', models.IntegerField(default=0)),
                ('half_baths', models.IntegerField(default=0)),
                ('parking', models.CharField(max_length=50)),
                ('parking_slots', models.IntegerField(default=0)),
                ('balcony', models.CharField(max_length=50)),
                ('basement', models.BooleanField(default=False)),
                ('storage', models.BooleanField(default=False)),
                ('legal_status', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=50)),
                ('efficiency', models.CharField(max_length=50)),
                ('efficiency_index', models.CharField(max_length=50)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listing')),
            ],
        ),
    ]
