# 1. Task to count all player objects - count_players

# 2. Task to Update Player DB - update_players_from_json
from .models import Player
from celery import shared_task
from datetime import datetime
import json
from django.conf import settings
import os


@shared_task
def count_players():
    
    count = Player.objects.count()
    
    return f"Number of Player : {count}"


def parse_date(date_str):
    if date_str:
        try:
            #Jun 24, 1987
            return datetime.strptime(date_str, "%b %d, %Y")
        except:
            return None
    else:
        None
        
@shared_task
def update_players_from_json():
    json_file_path = os.path.join(settings.BASE_DIR, 'player_data.json')
   
    with open(json_file_path, "r") as fp:
    
        player_data = json.load(fp)
    
    for player in player_data:
        player['date_of_birth'] = parse_date(player.get("date_of_birth"))
        player['contract_expires'] = parse_date(player.get("contract_expires"))
        player['joined_date'] = parse_date(player.get("joined_date"))
        
        Player.objects.update_or_create(
            id = player['id'],
            defaults=player
        )
            
