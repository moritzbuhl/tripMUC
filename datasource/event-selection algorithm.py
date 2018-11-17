#event-selection algorithm 
import numpy as np
from numpy.random import choice
ranges = [[1, 1],[2, 3],[3,5]] #[level, weight]
total_agenda = [[2,3,4],[4,6,8],[6,9,12],[8,12,16]]  #total_agenda[days-1][activities level-1]
#--------PRESET------where the input will put below-----#
#--------PRESET------where the input will put below-----#
#--------PRESET------where the input will put below-----#
landmark = 1
culture  = 3
shopping =5

days = 4 #range 1-4
level = 3 #range 1-3
#-----------------finished----------------------#

#act = [] #a list of all type of activities 

num_act = total_agenda[days-1][level-1] #actual number of activities 
choices = ['landmark', 'culture', 'shopping']

#------weight/probability-----#
weight = landmark + culture + shopping
wl = landmark/weight
wc = culture/weight
ws = shopping/weight
w = [wl, wc, ws]
print(weight)
cl = 1 
cc = 1
cs = 1 

while (cl > wl + 0.08) or (cc > wc + 0.08) or (cs > ws +0.08) :
	act = list(choice(choices, num_act, w))
	print(act)
	cl = act.count('landmark')/num_act

	cc = act.count('culture')/num_act
	cs = act.count('shopping')/num_act

ratio = [cl, cc, cs]
print(ratio)
print(act)


