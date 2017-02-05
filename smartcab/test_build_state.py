inputs = {'light': 'red', 'oncoming': 'right', 'left': 'forward', 'right': 'right'}

waypoint = 'left'

deadline =30

#list_state = inputs.items()
#list_state.append(('waypoint',waypoint))
#state = tuple(list_state)


list_state = []

# include light in state
list_state.append(('light', inputs['light']))

# include oncoming in state
list_state.append(('oncoming', inputs['oncoming']))

# inspect whether another driving left to the agent is driving forward
if inputs['right'] == 'forward':
    list_state.append(('right','true'))
else: 
    list_state.append(('right','false'))

# inspect whether another driving left to the agent is driving forward
if inputs['left'] == 'forward':
    list_state.append(('left','true'))
else: 
    list_state.append(('left','false'))
    
# include waypoint
list_state.append(('waypoint',waypoint))

# include deadline 
if deadline <= 7: 
    list_state.append(('deadline','true'))
else:
    list_state.append(('deadline','false'))

state = tuple(list_state)

print state, type(state),type(state[0])    
