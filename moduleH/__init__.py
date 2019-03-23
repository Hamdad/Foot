from moduleH.strategies import GardienStrategy,SoloStrategy4,SoloStrategy2, FonceurStrategy,DefenseStrategy, SoloStrategy, RandommmStrategy, RandommStrategy, RandomStrategy
from soccersimulator import SoccerTeam


def get_team(nb_players):
    team = SoccerTeam(name="Strange's Team")
    if nb_players == 1:
        team.add("F",SoloStrategy())
    if nb_players == 2:
        team.add("F",DefenseStrategy())
        team.add("F",SoloStrategy2())
       
    if nb_players == 4:
        team.add("S",SoloStrategy2())
        team.add("###",DefenseStrategy())
        team.add("S2",SoloStrategy4())
        team.add("###",GardienStrategy())
    return team
