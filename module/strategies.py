# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, settings
import math
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
       	return SoccerAction(Vector2D.create_random(-1.,1.),Vector2D.create_random(-1.,1.))


class AttaquantStrategy(Strategy):
    def _init_(self):
        """jgbuj"""
        Strategy._init_(self,"Attaquant")
        
    def compute_strategy(self,state,id_team,id_player):
        return
       # d=Vector2D(settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
       # b=state.ball.position-d
       # k=Vector2D(1,0)
  #      if b.dot(k):
    #      if id_team==1

                                                                                                                                                  
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
       	#return SoccerAction(Vector2D.create_random(-1.,1.),Vector2D.create_random(-1.,1.))
           ball=state.ball.position
           player=state.player_state(id_team,id_player).position
           #d=b-p
           if id_team==1:
               goal= Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
           else:
               goal = Vector2D(0,settings.GAME_HEIGHT/2)
           if player.distance(ball) < settings.PLAYER_RADIUS + settings.BALL_RADIUS:
               shoot_alt=goal-player
               if id_team==1:# ici on doit voir s'il y a un joueur a coté de la balle 
                   shoot_alt.scale(0)
               else:
                   shoot_alt.scale(0.01)
               return SoccerAction(shoot=shoot_alt)
           else:
               return SoccerAction(acceleration=ball-player)
           #return SoccerAction(d,Vector2D(1,0))

class TestStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Test")
        
    def compute_strategy(self, state, id_team, id_player):
           ball=state.ball.position
           player=state.player_state(id_team,id_player).position
           #d=b-p
           if id_team==1:
               goal= Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
           else:
               goal = Vector2D(0,settings.GAME_HEIGHT/2)
           if player.distance(ball) < settings.PLAYER_RADIUS + settings.BALL_RADIUS:
               shoot_alt=goal-player
               if id_team==1:# ici on doit voir s'il y a un joueur a coté de la balle 
                   shoot_alt.scale(0)
               else:
                   shoot_alt.scale(0.01)
               return SoccerAction(shoot=Shoot(state).to_goal2())
           else:
               return SoccerAction(acceleration=ball-player)
           #return SoccerAction(d,Vector2D(1,0)) 






class Move( object ): #MOVE et SHOOT copié du cours mode tevyas zat n chikh hhh et je sais pas pk on nous a demandé de les mettre dans un fichier actions.py  or qu'on nous a demandé d'avoir juste les 3 dans notre dossier.
    def __init__( self ,SupState):
            self.SupState=SupState
            
    def move(self, acceleration=None):
            return SoccerAction(acceleration=acceleration)
    def to_ball(self):
            return self.move(self.SupState.ball_dir()) 
        
        
        
        
class Shoot(object):
    def __init__(self, SupState):
        self.SupState=SupState

    def shoot(self, direction=None):
        if self.SupState.dist_ball() < settings.PLAYER_RADIUS + settings.BALL_RADIUS :
            return SoccerAction(shoot=direction)
        else :
            return SoccerAction()
        
    def to_goal(self, strength=1):
        return self.shoot(self.SupState.goal_dir()*strength) #remplacer goal_dir par but_adv  

    def to_goal2(self,direction, strength=1, ): #direction de la frappe
       return self.shoot(angle=math.pi/4.,norm=(self.Suptate.goal_dist()*2**-0.5)*2)
        
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Random", RandomStrategy())  # Random strategy
#team1.add("Fonceur1CR7", FonceurStrategy()) #Fonceur strategy
#team2.add("Fonceur2", FonceurStrategy()) #Fonceur strategy
team2.add("MESSI", TestStrategy()) #Fonceur strategy
print(team1.players,team2)
team2.add("Staatic", Strategy())   # Static strategy
# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)