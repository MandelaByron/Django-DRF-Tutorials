# Generated by Django 5.0.6 on 2024-05-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField(null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('place_of_birth', models.CharField(max_length=250, null=True)),
                ('place_of_birth_title', models.CharField(max_length=250, null=True)),
                ('place_of_birth_flag', models.URLField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('height', models.FloatField(null=True)),
                ('foot', models.CharField(max_length=10, null=True)),
                ('citizenship', models.JSONField(null=True)),
                ('citizenship_flag', models.JSONField(null=True)),
                ('headshot', models.URLField(null=True)),
                ('club', models.CharField(max_length=100)),
                ('club_logo', models.URLField(max_length=250, null=True)),
                ('main_position', models.CharField(null=True)),
                ('other_positions', models.JSONField(null=True)),
                ('national_team', models.CharField(null=True)),
                ('national_team_flag', models.URLField(null=True)),
                ('caps', models.IntegerField(null=True)),
                ('international_goals', models.IntegerField(null=True)),
                ('market_value', models.IntegerField(null=True)),
                ('league_name', models.CharField(max_length=100, null=True)),
                ('league_level', models.CharField(max_length=100, null=True)),
                ('league_logo', models.URLField(max_length=250, null=True)),
                ('joined_date', models.DateField(null=True)),
                ('contract_expires', models.DateField(null=True)),
                ('agency_info', models.JSONField(null=True)),
                ('club_stats', models.JSONField(null=True)),
                ('national_team_stats', models.JSONField(null=True)),
                ('current_season_stats', models.JSONField(null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id', 'market_value'], name='players_pla_id_7bc858_idx')],
            },
        ),
    ]
