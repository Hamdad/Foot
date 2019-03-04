from tools import GoalSearch
from strategies import GoTestStrategy

strength=[0]
gs=GoalSearch(GoTestStrategy(),{'strength':strength})
gs.start()
#print(gs.get_res())
#print(gs.get_best())
