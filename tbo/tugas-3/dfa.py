def hat_delta_dfa(delta_dfa: dict, state: str, x: str) -> str:
    if x == '':
        return state
    else:
        return delta_dfa[(hat_delta_dfa(delta_dfa, state, x[0:-1]), x[-1])]

def dfa(finals: set, delta_dfa: dict, x:str, q0: str) -> bool:
    return hat_delta_dfa(delta_dfa, q0, x) in finals
