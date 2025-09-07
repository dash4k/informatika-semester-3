from delta_nfa import l1_delta_nfa, l2_delta_nfa, l3_delta_nfa, l4_delta_nfa

def l1_hat_nfa(states, x) -> set:
    states = states
    for i in range(len(x)):
        curr = set()
        for state in states:
            curr = curr.union(l1_delta_nfa(state, x[i]))
        states = curr
    return states

def l2_hat_nfa(states, x) -> set:
    states = states
    for i in range(len(x)):
        curr = set()
        for state in states:
            curr = curr.union(l2_delta_nfa(state, x[i]))
        states = curr
    return states

def l3_hat_nfa(states, x) -> set:
    states = states
    for i in range(len(x)):
        curr = set()
        for state in states:
            curr = curr.union(l3_delta_nfa(state, x[i]))
        states = curr
    return states

def l4_hat_nfa(states, x) -> set:
    states = states
    for i in range(len(x)):
        curr = set()
        for state in states:
            curr = curr.union(l4_delta_nfa(state, x[i]))
        states = curr
    return states