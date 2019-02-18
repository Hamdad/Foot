#objets pour un match

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, settings
class SupState(object):

	def __init__(self,state,idteam,idplayer) :
		self.state = state
		self.key = (idteam, idplayer)
		self.but_adv = Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2) if self.key[0] == 1 else Vector2D(0, settings.GAME_HEIGHT/2)
		self.my_but = Vector2D(0, settings.GAME_HEIGHT/2) if self.key[0] == 1 else Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
		#recup joueur
		self.all_players = self.state.players
		self.co_players = [p  for p in self.all_players if (p[0] == self.key[0] and p[1] != self.key[1])]
		if len(self.co_players)==1 :
			self.co_player = self.co_players[0]
		if len(self.co_players)==1 :
			self.co_player_pos = self.state.player_state(self.co_player[0],self.co_player[1])
		self.adv_players = [p  for p in self.all_players if p[0] != self.key[0]]
		#variable pour avoir le sens pour pouvoir l'utiliser lors de changement ...
		self.sens = 1 if self.key[0] == 1 else -1

    #si le joueur peut tirer METHODEEEEEEEEEEEE
		self.my_position = self.state.player_state(self.key[0], self.key[1]).position
	#	|self.ball_position = c
    	#	|self.can_shoot = True if self.my_position.distance(self.ball_position) <= (settings.PLAYER_RADIUS + settings.BALL_RADIUS) else False
		#self.v_ball = self.state.ball.vitesse
    	#a revoir sans pitié
         # |self.adv_on_right = 1 if self.state.player_state(self.adv_players[0][0], self.adv_players[0][1]).position.y > self.my_position.y else -1
		self.my_v = self.state.player_state(self.key[0], self.key[1]).vitesse
		#est proche de la balle
	#	|self.near_ball = True if self.my_position.distance(self.ball_position) < settings.BALL_RADIUS else False


#    @property
	def proche_ball(self):
		me_ball = self.dist_ball()
		for p in self.all_players:
			pos_p = self.state.player_state(p[0], p[1]).position
			if me_ball > pos_p.distance(self.ball_position()) :
				return False
		return True
    
    
    
   # def ball_dir(self):
    #    return self.position-
    
    
  #  def infront(self):
   #     for player in self.adv_player:
            
            
#      def can_sh  
	"""def advfront(self):
        for player in self.adv_players:
            if player.position.x>self.my_position.x:
                if player.position.y=self.my_position.y"""

	@property
	def have_ball(self):
        	return self.my_position.distance(self.ball_position) < 1


	def ball_position(self):
            return self.state.ball.position

	def can_shoot(self):
            if self.my_position.distance(self.ball_position()) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS):
                return True
            return False


	def v_ball(self):
            return self.state.ball.vitesse

	def eclatement(self):
            l1=[] 
            l2=[] 
            l3=[] 
            l4=[] 
            l5=[] 
            l6=[] 
            l7=[] 
            l8=[] 
            l9=[]
            l10=[]
            l11=[]
            l12=[]
            l13=[]
            l14=[]
            l15=[]
            l16=[]
            for player in self.all_players:
                if player.position.x<settings.GAME_WIDTH//4:
                    if player.position.y<settings.GAME_HEIGHT//4:
                        l1.add(player)
                    elif player.position.y<settings.GAME_HEIGHT//2:
                        l5.add(player)
                    elif player.position.y<3*settings.GAME_HEIGHT//4:
                        l9.add(player)
                    else:
                        l12.add(player)
                elif player.position.x<settings.GAME_WIDTH//2:
                    if player.position.y<settings.GAME_HEIGHT//4:
                        l2.add(player)
                    elif player.position.y<settings.GAME_HEIGHT//2:
                        l6.add(player)
                    elif player.position.y<3*settings.GAME_HEIGHT//4:
                        l10.add(player)
                    else:
                        l14.add(player)                           
                elif player.position.x<3*settings.GAME_WIDTH//4:
                    if player.position.y<settings.GAME_HEIGHT//4:
                        l.add(player) #############a9lin dayi
                    elif player.position.y<settings.GAME_HEIGHT//2:
                        l10.add(player)
                    elif player.position.y<3*settings.GAME_HEIGHT//4:
                        l11.add(player)
                    else:
                        l12.add(player)   
                else:
                    if player.position.y<settings.GAME_HEIGHT//4:
                        l13.add(player)
                    elif player.position.y<settings.GAME_HEIGHT//2:
                        l14.add(player)
                    elif player.position.y<3*settings.GAME_HEIGHT//4:
                        l15.add(player)
                    else:
                        l16.add(player)              
                                    #a completer
             
                return [[l1,l2,l3,l4],[l5]]
	def coeq_proche(self):
		return [p for p in self.co_players if self.my_position.distance(self.state.player_state(p[0], p[1]).position) < (settings.GAME_WIDTH/2)] #A revoir et werna mlih ^-^

	def my_vit(self):
		return self.state.player_state(self.key[0], self.key[1]).vitesse

	def near_ball(self):
		if self.my_position.distance(self.ball_position) < settings.BALL_RADIUS:
			return True
		return False


	def dist_ball(self):
		return self.my_position.distance(self.ball_position())


	def dist_but_adv(self):
		return self.my_position.distance(self.but_adv)


	def dist_my_but(self):
		return self.my_position.distance(self.my_but)


	def pos_adv_nearby(self):
     		return min([(self.player.distance(player),player) for player in self.adv_players])[1]


	def dist_adv_nearby(self):
		return min([(self.player.distance(player),player) for player in self.adv_players])[0]
    
	def dist_my_wall(self):
		if self.my_position.y>settings.GAME_HEIGHT/2:
			return settings.GAME_HEIGHT - self.my_position.y
		return self.my_position.y

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


	#@property
	def aller_ball(self) :
		#les cas ou je suis proche de la balle et elle va vite?
		k = (self.v_ball()*3+(self.ball_position() - self.my_position))
		joue = SoccerAction(acceleration = k)
		if self.dist_ball() > 11:
			return joue
		elif self.dist_ball() > 4:
			return SoccerAction(acceleration=(self.ball_position() - self.my_position)/2)
		else :
			return SoccerAction(acceleration=(self.ball_position() - self.my_position).normalize())


	def predict_ball(self):
		norm_base = self.v_ball().norm
		norm_tour = self.v_ball().norm - settings.ballBrakeSquare * self.v_ball().norm ** 2 - settings.ballBrakeConstant * self.v_ball().norm
		norm_fin = norm_base *2 - norm_tour
		ball_pos_fin = self.ball_position() + (self.v_ball().normalize() * norm_fin)
		return ball_pos_fin