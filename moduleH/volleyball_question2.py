
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam , settings
from soccersimulator import VolleySimulation, volley_show_simu
import math
from tools import SupState


class Attaque(Strategy):
    def __init__ (self):
        Strategy . __init__ (self , "Echauffement")
        
    def compute_strategy (self , state , id_team , id_player):
        sup = SupState(state , id_team , id_player)
        if sup.can_shoot():
            #print(sup.adv_players_pos[0])
            if sup.dist_my_fillet() < 30:
                if sup.adv_players_pos[0].y < settings.GAME_HEIGHT/2:    
                    if sup.dist_wall_adv()[0] <20 :
                        return SoccerAction( shoot = (sup.adv_players_pos[0] + settings.GAME_HEIGHT/2 - sup.my_position)*0.1)
                    else : 
                        return SoccerAction(shoot = (sup.adv_players_pos[0] + 2*sup.dist_wall_adv()[1]/3 - sup.my_position)*0.1)
                else :
                    if sup.dist_wall_adv()[0] <20 :
                        return SoccerAction( shoot = (sup.adv_players_pos[0] - settings.GAME_HEIGHT/2 - sup.my_position)*0.1)
                    else : 
                        return SoccerAction(shoot = (sup.adv_players_pos[0] - 2*sup.dist_wall_adv()[1]/3 - sup.my_position)*0.1)
                    
            return SoccerAction(shoot = Vector2D(2*sup.sens , 0) ,  acceleration = Vector2D(20*sup.sens , 0))
        elif sup.ball_ds_mn_terrain():
            return SoccerAction(acceleration = sup.predict_ball() - sup.my_position)
        else : 
            return SoccerAction(acceleration = (Vector2D(45,45)if sup.sens == 1 else Vector2D(135,45)) - sup.my_position)

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Attaque())  # Random strategy
team2.add("Player 2", Attaque())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
