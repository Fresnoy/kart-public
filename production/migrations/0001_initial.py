# Generated by Django 4.1 on 2024-08-28 13:35

import common.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        ('common', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InstallationGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('label_fr', models.CharField(max_length=255)),
                ('label_en', models.CharField(max_length=255)),
                ('description_fr', models.TextField()),
                ('description_en', models.TextField()),
                ('gallery', models.ManyToManyField(blank=True, related_name='itineraries', to='assets.gallery')),
            ],
            options={
                'verbose_name_plural': 'itineraries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('former_title', models.CharField(blank=True, max_length=255, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(blank=True, upload_to=common.utils.make_filepath)),
                ('description_short_fr', models.TextField(blank=True, null=True)),
                ('description_short_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='StaffTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('production_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='production.production')),
                ('production_date', models.DateField()),
                ('credits_fr', models.TextField(blank=True, null=True)),
                ('credits_en', models.TextField(blank=True, null=True)),
                ('thanks_fr', models.TextField(blank=True, null=True)),
                ('thanks_en', models.TextField(blank=True, null=True)),
                ('copyright_fr', models.TextField(blank=True, null=True)),
                ('copyright_en', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('production.production',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('production_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='production.production')),
                ('main_event', models.BooleanField(default=False, help_text='Meta Event')),
                ('type', models.CharField(choices=[('FEST', 'Festival'), ('COMP', 'Competition'), ('PROJ', 'Projection'), ('EXHIB', 'Exhibition'), ('VARN', 'Varnishing'), ('PARTY', 'Party'), ('WORKSHOP', 'Workshop'), ('EVENING', 'Evening')], max_length=10)),
                ('starting_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('production.production',),
        ),
        migrations.CreateModel(
            name='ProductionStaffTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_tasks', to='production.production')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.staff')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='production.stafftask')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductionOrganizationTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.organization')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organization_tasks', to='production.production')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='production.organizationtask')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='production',
            name='collaborators',
            field=models.ManyToManyField(blank=True, related_name='%(class)s', through='production.ProductionStaffTask', to='people.staff'),
        ),
        migrations.AddField(
            model_name='production',
            name='partners',
            field=models.ManyToManyField(blank=True, related_name='%(class)s', through='production.ProductionOrganizationTask', to='people.organization'),
        ),
        migrations.AddField(
            model_name='production',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='production',
            name='websites',
            field=models.ManyToManyField(blank=True, to='common.website'),
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='production.event')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('production.event',),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('artwork_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='production.artwork')),
                ('duration', models.DurationField(blank=True, help_text='Sous la forme HH:MM:SS', null=True)),
                ('shooting_format', models.CharField(blank=True, choices=[('SUP8', 'Super 8'), ('SUP16', 'Super 16'), ('SUP35', 'Super 35'), ('35MM', '35 MM'), ('70MM', '70 MM'), ('DV', 'DV'), ('DVCAM', 'DV-CAM'), ('HD', 'HD'), ('HDCAM', 'HD-CAM'), ('HDCINE', 'HD CINEMASCOPE'), ('CREANUM', 'CREATION NUMERIQUE'), ('BETASP', 'BETA SP'), ('BETANUM', 'BETA NUM.'), ('DIGICAM', 'APPAREIL PHOTO'), ('MOBILE', 'MOBILE'), ('HI8', 'HI8'), ('AVCHD', 'AVCHD'), ('XDCAMEX', 'XDcamEX'), ('3DREL', 'RELIEF 3D'), ('2K', '2K'), ('4K', '4K')], max_length=10)),
                ('aspect_ratio', models.CharField(blank=True, choices=[('1.33', '1.33 (4/3)'), ('1.37', '1.37'), ('1.66', '1.66'), ('1.77', '1.77 (16/9)'), ('1.85', '1.85 (Flat)'), ('1.90', '1.90 (Full Container)'), ('2.39', '2.39 (Scope)')], max_length=10)),
                ('process', models.CharField(blank=True, choices=[('COLOR', 'Couleur'), ('BW', 'Noir & Blanc'), ('COLORBW', 'NB & Couleur'), ('SEPIA', 'Sépia')], max_length=10)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('production.artwork',),
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('artwork_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='production.artwork')),
                ('technical_description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('production.artwork',),
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('artwork_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='production.artwork')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('production.artwork',),
        ),
        migrations.CreateModel(
            name='ItineraryArtwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.itinerary')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.artwork')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='itinerary',
            name='artworks',
            field=models.ManyToManyField(through='production.ItineraryArtwork', to='production.artwork'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='event',
            field=models.ForeignKey(limit_choices_to={'type': 'EXHIB'}, on_delete=django.db.models.deletion.PROTECT, related_name='itineraries', to='production.event'),
        ),
    ]
