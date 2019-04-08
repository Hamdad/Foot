
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
                #print("inon")
                return sup.shoot_fil()
            else :return SoccerAction(shoot = Vector2D(20*sup.sens , 0) ,  acceleration = Vector2D(20*sup.sens , 0))
            
        elif sup.ball_ds_mn_terrain() and sup.proche_ball():
            return SoccerAction(acceleration = sup.ball_position() - sup.my_position)
        else : 
            return SoccerAction(acceleration = (Vector2D(80,sup.ball_position().y)if sup.sens == 1 else Vector2D(100,sup.ball_position().y)) - sup.my_position)

class Def2(Strategy):
    def __init__ (self):
        Strategy . __init__ (self , "Echauffement")
        
    def compute_strategy (self , state , id_team , id_player):
        sup = SupState(state , id_team , id_player)
        if sup.can_shoot():
            return SoccerAction(shoot =(sup.co_player_pos - sup.my_position).norm_max(4))
        if sup.ball_ds_mn_terrain() and sup.proche_ball():
            return SoccerAction(acceleration = sup.predict_ball() - sup.my_position)
        else : 
            return SoccerAction(acceleration = (Vector2D(45,sup.predict_ball().y)if sup.sens == 1 else Vector2D(135,sup.predict_ball().y)) - sup.my_position)

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        return SoccerAction(acceleration=Vector2D.create_random(-1, 1),
                            shoot=Vector2D.create_random(-1, 1))


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Solo())  # Random strategy
team1.add("P1 Def", Def2())
team2.add("Player 2", Solo())   # Random strategy
team2.add("Random2",RandomStrategy())
# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
