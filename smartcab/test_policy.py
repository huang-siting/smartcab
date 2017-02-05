def  test_policy(Q):
        
    violation = 0
    policy_evaluation = dict()

    for state in Q:
        action =  max(Q[state], key = Q[state].get) 

        light = state[0][1] 
        oncoming = state[1][1] 
        is_right_forward = state[2][1] 
        is_left_forward = state[3][1] 
        waypoint = state[4][1] 
        is_deadline_close = state[5][1] 

        # Agent wants to drive forward:
        if action == 'forward':
            if light != 'green': # Running red light
                violation = 2 # Major violation
                if is_left_forward == 'true' or is_right_forward == 'true': # Cross traffic
                    violation = 4 # Accident

        if violation == 4: 
            print "{}\n".format(state)

            for action, reward in Q[state].iteritems():
                print " -- {} : {:.2f}\n".format(action, reward)
                print "\n"

        policy_evaluation[state] = violation
        violation = 0






