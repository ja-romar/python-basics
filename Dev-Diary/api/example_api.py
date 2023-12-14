#Example of how to use an API

from nba_api.stats.static import teams
import matplotlib.pyplot as plt 

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
        return out_dict
    
nba_teams = teams.get_teams()

nba_teams[0:3]

