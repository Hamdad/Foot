from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, settings
import math
from tools import SupState
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


"""class Defense(Strategy):
	def __init__(self, name="defense"):
		Strategy.__init__(self, name)
	def compute_strategy(self,state, idteam, idplayer):
 






"""

                                                                                                                                                  
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

class SoloStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Test")
        
    def compute_strategy(self, state, id_team, id_player):
        ball=state.ball.position
        player=state.player_state(id_team,id_player).position
        sup=SupState(state,id_team,id_player)
           #d=b-p
        # if sup.dist_but_adv()>settings.GAME_WIDTH//2:   
        if player.y>2*settings.GAME_HEIGHT/3 or player.y<settings.GAME_HEIGHT/3:                  
            if player.distance(ball) < settings.PLAYER_RADIUS + settings.BALL_RADIUS:
                 if(sup.dist_but_adv()<settings.GAME_WIDTH/4): 
                      return SoccerAction(shoot=sup.but_adv-sup.my_position)
                 return (Shoot2(sup).to_goal2()+SoccerAction(acceleration=Vector2D(1,0)))
            else:
                  return SoccerAction(acceleration=ball-player)                 
        else:
            if player.distance(ball) < settings.PLAYER_RADIUS + settings.BALL_RADIUS:
                  if(sup.dist_but_adv()<settings.GAME_WIDTH/4): 
                      return SoccerAction(shoot=sup.but_adv-sup.my_position)
                  else:
                      pshoot=sup.but_adv-sup.my_position   
                      return SoccerAction(shoot=pshoot.scale(0.02))
            else:
                  return SoccerAction(acceleration=ball-player)      
          






	#else:
               #    return SoccerAction(acceleration=ball-player)
           #return SoccerAction(d,Vector2D(1,0)) 
         #  else:
           #    Shoot2(sup).shoot2(sup.but_adv-sup.my_position)
               
               

"""class Solo(Strategy):
    def __init__(self,name):
        Strategy.__init__(self,"SoloStrategy")
    def compute_strategy(self,state,idteam,idplayer):        
    
   """ 
        
                          
    

class Move(object): #MOVE et SHOOT copié du cours mode tevyas zat n chikh hhh et je sais pas pk on nous a demandé de les mettre dans un fichier actions.py  or qu'on nous a demandé d'avoir juste les 3 dans notre dossier.
    def __init__( self ,SupState):
            self.SupState=SupState
            
    def move(self, acceleration=None):
            return SoccerAction(acceleration=acceleration)
    def to_ball(self):
            return self.move(self.SupState.ball_dir()) 
        
        
        
        
class Shoot2(object):
    def __init__(self, SupState):
        self.SupState=SupState

    def shoot2(self, direction=None):
        if self.SupState.dist_ball() < settings.PLAYER_RADIUS + settings.BALL_RADIUS:
            return SoccerAction(shoot=direction)
        else :
            return SoccerAction(acceleration=self.SupState.ball_position-self.SupState.my_position)
        
    def to_goal(self, strength=1):
        return self.shoot2(self.SupState.goal_dir()*strength) #remplacer goal_dir par but_adv  

    def to_goal2(self): #direction de la frappe
     # return self.shoot2(direction=Vector2D(0,50))
     #print(((self.SupState.dist_but_adv()*2**-0.5)*2))
     qte=(2*math.sqrt(2*(((1/4)*settings.GAME_WIDTH)**2)))
     qte2=math.sqrt(qte)
     if self.SupState.sens ==1:
         if self.SupState.my_position.y>settings.GAME_HEIGHT/2:    
             return SoccerAction(shoot=Vector2D(angle=1*(math.pi/4.),norm=qte))+SoccerAction(acceleration=Vector2D(self.SupState.sens*qte2,0))
         return  SoccerAction(shoot=Vector2D(angle=7*(math.pi/4.),norm=qte))+SoccerAction(acceleration=Vector2D(self.SupState.sens*qte2,0))   
     else:
         if self.SupState.my_position.y>settings.GAME_HEIGHT/2:
             return SoccerAction(shoot=Vector2D(angle=3*(math.pi/4.),norm=qte))+SoccerAction(acceleration=Vector2D(self.SupState.sens*qte2,0))
         return  SoccerAction(shoot=Vector2D(angle=5*(math.pi/4.),norm=qte))+SoccerAction(acceleration=Vector2D(self.SupState.sens*qte2,0))   
     
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
#team1.add("Random",FonceurStrategy())  # Random strategy
#team1.add("Random3",FonceurStrategy()) 
team1.add("ASSIREM",SoloStrategy()) 
team1.add("3PILA", SoloStrategy())
#team1.add("Fonceur1CR7", FonceurStrategy()) #Fonceur strategy
#team2.add("Fonceur2", FonceurStrategy()) #Fonceur strategy
team2.add("LYES", SoloStrategy())
team2.add("3PILA", FonceurStrategy())
 #Fonceur strategy
print(team1.players,team2)
#team2.add("Staatic", Strategy())   # Static strategy
# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)

