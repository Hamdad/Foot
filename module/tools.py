from ..soccersimulator import SoccerState

#objets pour un match

from ..soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, settings

class SupState(object):

	def __init__(self,state,idteam,idplayer) :
		self.state = state
		self.key = (idteam, idplayer)
		self.but_adv = Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2) if self.key[0] == 1 else Vector2D(0, settings.GAME_HEIGHT/2)
		self.but = Vector2D(0, settings.GAME_HEIGHT/2) if self.key[0] == 1 else Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
		#recup joueur
		self.all_players = self.state.players
		self.co_players = [p  for p in self.all_players if (p[0] == self.key[0] and p[1] != self.key[1])]
		self.adv_players = [p  for p in self.all_players if p[0] != self.key[0]]
		#variable pour avoir le sens pour pouvoir l'utiliser lors de changement ...
		self.sens = 1 if self.key[0] == 1 else -1

    #si le joueur peut tirer METHODEEEEEEEEEEEE
    		|self.my_position = self.state.player_state(self.key[0], self.key[1]).position
		|self.ball_position = c
    		|self.can_shoot = True if self.my_position.distance(self.ball_position) <= (settings.PLAYER_RADIUS + settings.BALL_RADIUS) else False
		|self.v_ball = self.state.ball.vitesse
    	#a revoir sans pitié
          |self.adv_on_right = 1 if self.state.player_state(self.adv_players[0][0], self.adv_players[0][1]).position.y > self.my_position.y else -1
		|self.my_v = self.state.player_state(self.key[0], self.key[1]).vitesse
		#est proche de la balle
		|self.near_ball = True if self.my_position.distance(self.ball_position) < settings.BALL_RADIUS else False

		#liste des coeq proche
          |self.coeq_proche = [p for p in self.co_players if self.my_position.distance(self.state.player_state(p[0], p[1]).position) < (settings.GAME_WIDTH/2)]
		#distance de la balle
		|self.dist_ball = self.my_position.distance(self.ball_position)
		|self.dist_but_adv = self.my_position.distance(self.but_adv)
		|self.dist_but_mine = self.my_position.distance(self.but)


    @property
	def proche_ball(self):
		me_ball = self.dist_ball
		for p in self.all_players:
			pos_p = self.state.player_state(p[0], p[1]).position
			if me_ball > pos_p.distance(self.ball_position) :
				return False
		return True

	@property
	def have_ball(self):
		return self.my_position.distance(self.ball_position) < 1


#def adv_list(self):
#   return [self.state.player_state(id_team,id_player).position for(id_team,id_player) in self]
	@property
     def my_position(self):
            return self.state.player_state(self.key[0], self.key[1]).position

	@property
     def ball_position(self):
            return self.state.ball.position
	@property
     def can_shoot(self):
            if self.my_position.distance(self.ball_position) <= (settings.PLAYER_RADIUS + settings.BALL_RADIUS):
                return True
            return False

	@property
     def v_ball(self):
            return self.state.ball.vitesse

   # def adv_on_right(self):
        #a compléter
	@property
	def coeq_proche(self):
       return [p for p in self.co_players if self.my_position.distance(self.state.player_state(p[0], p[1]).position) < (settings.GAME_WIDTH/2)] #A revoir et werna mlih ^-^

   @property
    def my_vit(self):
    	return self.state.player_state(self.key[0], self.key[1]).vitesse

	@property
    def near_ball(self):
    	if self.my_position.distance(self.ball_position) < settings.BALL_RADIUS:
        	return True
        return False

	@property
	def dist_ball(self):
          return self.my_position.distance(self.ball_position)

 	 @property
	 def dist_but_adv(self):
         return self.my_position.distance(self.but_adv)

 	 @property
	 def dist_mon_but(self):
         return self.my_position.distance(self.but)

	 @property
	 def pos_adv_nearby(self):
     		return min([(self.player.distance(player),player) for player in self.adv_players])[1]

	@property
	def dist_adv_nearby(self):
		return min([(self.player.distance(player),player) for player in self.adv_players])[0]

	@property
	def coeq_libre(self) :
		if len(self.coeq_proche) == 0 :
			return [0, 0]
		elif len(self.coeq_proche) == 1 :
			return self.coeq_proche[0]
		else :
			p = self.coeq_proche[0]
			d = self.adv_nearby(self.state.player_state(p[0], p[1]).position) #position de p
			x = self.state.player_state(p[0], p[1]).position.distance(self.state.player_state(d[0], d[1]).position)
			pp = self.coeq_proche[0]
			for p in self.coeq_proche[1:] :
				#position de l'adv le plus proche de du coeq le plus proche
				a = self.adv_nearby(self.state.player_state(p[0], p[1]).position)
				ap = self.state.player_state(a[0], a[1]).position
				d = self.state.player_state(p[0], p[1]).position.distance(ap)
				if x < d :
					x = d
					pp = p
		return pp


	@property
	def aller_ball(self) :
		#les cas ou je suis proche de la balle et elle va vite?
		k = (self.v_ball*3+(self.ball_position - self.my_position))
		joue = SoccerAction(k, Vector2D())
		if self.dist_ball > 11:
			return joue
		elif self.dist_ball > 4:
			return SoccerAction((self.ball_position - self.my_position)/2, Vector2D())
		else :
			return SoccerAction((self.ball_position - self.my_position).normalize(), Vector2D())


	@property
	def predict_ball(self):
		norm_base = self.v_ball.norm
		norm_tour = self.v_ball.norm - settings.ballBrakeSquare * self.v_ball.norm ** 2 - settings.ballBrakeConstant * self.v_ball.norm
		norm_fin = norm_base *2 - norm_tour
		ball_pos_fin = self.ball_position + (self.v_ball.normalize() * norm_fin)
		return ball_pos_fin