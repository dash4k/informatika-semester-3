def hat_delta_nfa(delta_nfa: dict, states: set, x: str) -> set:
    states = states
    for char in x:
        curr = set()
        for state in states:
            if (state, char) in delta_nfa:
                curr = curr.union(delta_nfa[(state, char)])
        states = curr
    return states

def l_nfa(finals: set, delta_nfa: dict, x: str, q0: set) -> bool:
    return True if finals.intersection(hat_delta_nfa(delta_nfa, q0, x)) != set() else False