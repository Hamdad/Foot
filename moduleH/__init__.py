from moduleH.strategies import SoloStrategy, FonceurStrategy
from soccersimulator import SoccerTeam


def get_team(nb_players):
    team = SoccerTeam(name="Strange's Team")
    if nb_players == 1:
        team.add("F",FonceurStrategy())
    if nb_players == 2:
        team.add("S",SoloStrategy())
        #team.add("###",SoloStrategy())
    return team