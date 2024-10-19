import itertools

def states(nfa_states: set) -> set:
    return {subset for subset in itertools.chain.from_iterable(itertools.combinations(nfa_states, r) for r in range(len(nfa_states) + 1))}

def finals(nfa_finals: set, dfa_states: set) -> set:
    dfa_finals = set()
    for state in dfa_states:
        if nfa_finals.intersection(state) != set():
            dfa_finals.add(''.join(state))
    return dfa_finals

def deltas(delta_nfa: dict, dfa_states: set, lang: set, q0: set) -> dict:
    result = {}
    curr_states = {frozenset(q0)}
    visited = set(curr_states) 
    while curr_states:
        current = curr_states.pop() 
        for sigma in lang:
            next_states = set()
            for state in current:
                if (state, sigma) in delta_nfa:
                    next_states.update(delta_nfa[(state, sigma)])
            if next_states == set():
                next_states = {"Dead"}
            if next_states:
                next_fset = frozenset(next_states)
                result[(current, sigma)] = next_fset
                if next_fset not in visited:
                    visited.add(next_fset)
                    curr_states.add(next_fset)
    return result

def simplified(delta_dfa: dict) -> dict:
    sda = {}
    for (state, sigma), value in delta_dfa.items():
        sda[(''.join(state), sigma)] = ''.join(value)
    return sda