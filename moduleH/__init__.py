from moduleH.strategies import SoloStrategy3,SoloStrategy2, FonceurStrategy, DefenseStrategy,DefenseStrategy2, SoloStrategy
from soccersimulator import SoccerTeam


def get_team(nb_players):
    team = SoccerTeam(name="Strange's Team")
    if nb_players == 1:
        team.add("F",SoloStrategy())
    if nb_players == 2:
        team.add("S",SoloStrategy2())
        team.add("###",DefenseStrategy())
    if nb_players == 3:
        team.add("F",FonceurStrategy())
        team.add("F",FonceurStrategy())
        team.add("F",FonceurStrategy())
    if nb_players == 4:
         team.add("S3",SoloStrategy3())
        team.add("D",DefenseStrategy())
        team.add("G",DefenseStrategy2())
        team.add("A",SoloStrategy2())
          
    return team
