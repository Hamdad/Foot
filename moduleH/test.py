from tools import GoalSearch
from strategies import GoTestStrategy

strength=[0.1,0.2,0.3,0.4,0.5,1,1.2,1.9,2.5,3,3.5,4,4.6,5,5.5,6]
gs=GoalSearch(GoTestStrategy(),{'strength':strength})
gs.start()
print(gs.get_res())
print(gs.get_best())
