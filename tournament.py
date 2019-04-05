#from "notre dossier" import "nos strategies"

import Nasser

if __name__ == '__main__':
    from soccersimulator import Simulation, show_simu
    from moduleH import get_team
    
    #Test avec 1 et 2 joueurs
    team1 = Nasser.get_team(4)
    team2 = get_team(4)
    
    # Create a match 
    simulation1 = Simulation(team2,team1)
    
    # Simulate and display the match
    show_simu(simulation1)
    
    #Deuxieme simulation 2 vs 2 
    #team2_2 = get_team(2)
    
    #Lancement de la simulation 
    #simulation2 = Simulation(team2,team2_2)
    #show_simu(simulation2)
    
