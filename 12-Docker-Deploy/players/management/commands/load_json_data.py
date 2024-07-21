import json
from players.models import Player
from django.core.management.base import BaseCommand
from datetime import datetime
import os
from django.conf import settings
from django.db import transaction
class Command(BaseCommand):
    
    help = "Load data from JSON file"
    
    def handle(self, *args, **kwargs):
        path = os.path.join(settings.BASE_DIR, 'cleaned_player_data.json')
        with open(path, "r") as fp:
            
            player_data = json.load(fp)
            
            def parse_date(date_str):
                if date_str:
                    try:
                        #Jun 24, 1987
                        return datetime.strptime(date_str, "%b %d, %Y")
                    except:
                        return None
                else:
                    None
                    
            with transaction.atomic():
                for player in player_data:
                    player['date_of_birth'] = parse_date(player.get("date_of_birth"))
                    player['contract_expires'] = parse_date(player.get("contract_expires"))
                    player['joined_date'] = parse_date(player.get("joined_date"))
                    
                    Player.objects.update_or_create(
                        id = player['id'],
                        defaults=player
                    )
                    #Player.objects.create(**player)
                
            self.stdout.write(self.style.SUCCESS("Data loaded Successfully"))
        
        
