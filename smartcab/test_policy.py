import agent

def test_uniqueness(sim):
    """ test whether there is multiple actions with same highest Q value for all states"""

    Q = sim.env.primary_agent.Q 
    
    for state in Q: 
        maxQ = sim.env.primary_agent.get_maxQ(state)
        maxQ_actions = []
        for action in Q[state]: 
            if Q[state][action] == maxQ:  
                maxQ_actions.append(action) 
            if len(maxQ_actions)>1: 
                print "action is not unique"
                print "{}\n".format(state)
    
                for action, reward in Q[state].iteritems():
                    print " -- {} : {:.2f}\n".format(action, reward)
                    print "\n"

def violation_score(action, light, left, oncoming): 
    """ return violation score based on traffic rule"""

    violation = 0

    # Agent wants to drive forward:
    if action == 'forward':
        if light != 'green': # Running red light
            violation = 2 # Major violation
            if left == 'forward':
                violation = 4 # Accident

    # Agent wants to drive left:
    elif action == 'left':
        if light != 'green': # Running a red light
            violation = 2 # Major violation
            if left == 'forward': # Cross traffic
                violation = 4 # Accident
            elif oncoming == 'right': # Oncoming car turning right
                violation = 4 # Accident
        else: # Green light
            if oncoming == 'right' or oncoming == 'forward': # Incoming traffic
                violation = 3 # Accident

    # Agent wants to drive right:
    elif action == 'right':
        if light != 'green' and left == 'forward': # Cross traffic
            violation = 3 # Accident

    # Agent wants to perform no action:
    elif action == None:
        if light == 'green' and oncoming != 'left': # No oncoming traffic
            violation = 1 # Minor violation

    return violation


def test_safety(sim):
    """ print out action that violates traffic rule"""
    
    Q = sim.env.primary_agent.Q 
        
    for state in Q:
        action =  max(Q[state], key = Q[state].get) 

        waypoint = state[0][1] 
        light = state[1][1] 
        left = state[2][1] 
        oncoming = state[3][1] 
        
        violation = violation_score(action, light, left, oncoming) 

        # print the policies that violates traffic rule:
        if violation != 0: 
            print "action violates traffic rule"
            print "{}\n".format(state)

            for action, reward in Q[state].iteritems():
                print " -- {} : {:.2f}\n".format(action, reward)
                print "\n"


def test_reliability(sim):

    Q = sim.env.primary_agent.Q 
        
    for state in Q:
        action =  max(Q[state], key = Q[state].get) 

        waypoint = state[0][1] 
        light = state[1][1] ,
        left = state[2][1] 
        oncoming = state[3][1] 
    
        if action != waypoint: #agent doesn't drive to destination 
            if  violation_score(waypoint, light, left, oncoming) == 0: #taking waypoint as action is safe
                print "agent doesn't drive to destination when it's safe to do so:"
                print "{}\n".format(state)

                for action, reward in Q[state].iteritems():
                    print " -- {} : {:.2f}\n".format(action, reward)
                    print "\n"

