
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam , settings
from soccersimulator import VolleySimulation, volley_show_simu
import math
from tools import SupState


class Solo(Strategy):
    def __init__ (self):
        Strategy . __init__ (self , "Echauffement")
        
    def compute_strategy (self , state , id_team , id_player):
        sup = SupState(state , id_team , id_player)
        if sup.can_shoot():
            if sup.dist_my_fillet() < 30:
                return sup.shoot_fil()
            return SoccerAction(shoot = Vector2D(2*sup.sens , 0) ,  acceleration = Vector2D(20*sup.sens , 0))
            
        elif sup.ball_ds_mn_terrain():
            return SoccerAction(acceleration = sup.predict_ball() - sup.my_position)
        else : 
            return SoccerAction(acceleration = (Vector2D(45,45)if sup.sens == 1 else Vector2D(135,45)) - sup.my_position)

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Solo())  # Random strategy
team2.add("Player 2", Solo())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
