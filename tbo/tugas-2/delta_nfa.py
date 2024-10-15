def l1_delta_nfa(state, x) -> set:
    if state == 'A':
        return {'B'} if x == '1' else set()
    elif state == 'B':
        return {'C'} if x == '0' else set()
    elif state == 'C':
        return {state, 'D'} if x == '0' else {state}
    elif state == 'D':
        return {'E'} if x == '1' else set()
    else:
        return set()

def l2_delta_nfa(state, x) -> set:
    if state == 'A':
        return {state, 'B'} if x == '0' else {state}
    elif state == 'B':
        return {'C'} if x == '0' else set()
    elif state == 'C':
        return {'D'} if x == '0' else set()
    elif state == 'D':
        return {state, 'E'} if x == '1' else {state}
    else:
        return set()

def l3_delta_nfa(state, x) -> set:
    if state == 'A':
        return {'B'} if x == '0' else {'D'}
    elif state == 'B':
        return {state, 'C'} if x == '1' else {state}
    elif state == 'D':
        return {state, 'E'} if x == '0' else {state}
    else:
        return set()

def l4_delta_nfa(state, x) -> set:
    if state == 'A':
        return {'B'} if x == '0' else {'G'}
    elif state == 'B':
        return {state, 'C'} if x == '1' else {state}
    elif state == 'C':
        return {'D'} if x == '0' else set()
    elif state == 'D':
        return {'E'} if x == '1' else set()
    elif state == 'E':
        return {state, 'F'} if x == '0' else {state}
    elif state == 'G':
        return {'H'} if x == '0' else {state}
    elif state == 'H':
        return {'J'} if x == '0' else {'I'}
    elif state == 'I':
        return {'K'} if x == '0' else {state}
    elif state == 'J':
        return {'G'} if x == '1' else {state}
    elif state == 'K':
        return {'I'} if x == '1' else {state}
    else:
        return set()