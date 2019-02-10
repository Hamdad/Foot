#from "notre dossier" import "nos strategies"
from soccersimulator import SoccerTeam

def get_team(nb_players):
    team = SoccerTeam(name="Strange's Team")
    if nb_players == 1:
        team.add("CR7",SoloStrategy())
    if nb_players == 2:
        team.add("CR7",SoloStrategy())
        team.add("DYBALA",SoloStrategy())
    return team


if __name__ == '__main__':
    from soccersimulator import Simulation, show_simu
    
    #Test avec 1 et 2 joueurs
    team1 = get_team(1)
    team2 = get_team(2)
    
    # Create a match 
    simulation1 = Simulation(team1,team2)
    
    # Simulate and display the match
    show_simu(simulation1)
    
    #Deuxieme simulation 2 vs 2 
    team2_2 = get_team(2)
    
    #Lancement de la simulation 
    simulation2 = Simulation(team2,team2_2)
    show_simu(simulation2)
    
