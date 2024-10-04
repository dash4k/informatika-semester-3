def l1_delta(state, x) -> str:
    if state == 'A':
        return 'B' if x == '0' else 'C'
    elif state == 'B':
        return state
    elif state == 'C':
        return 'D' if x == '0' else 'B'
    elif state == 'D':
        return 'E' if x == '0' else state
    elif state == 'E':
        return 'F' if x == '1' else state
    else:
        return 'E' if x == '0' else 'D'

def l2_delta(state, x) -> str:
    if state == 'A':
        return 'B' if x == '0' else state
    elif state == 'B':
        return 'C' if x == '0' else 'A'
    elif state == 'C':
        return 'D' if x == '0' else 'A'
    elif state == 'D':
        return 'E' if x == '1' else state
    else:
        return 'D'

def l3_delta(state, x) -> str:
    if state == 'A':
        return 'B' if x == '1' else 'D'
    elif state == 'B':
        return 'C' if x == '0' else 'B'
    elif state == 'C':
        return 'B' if x == '1' else state
    elif state == 'D':
        return 'E' if x == '1' else state
    else:
        return 'D' if x == '0' else state

def l4_delta(state, x) -> str:
    if state == 'A':
        return 'B' if x == '0' else 'G'
    elif state == 'B':
        return 'C' if x == '1' else 'B'
    elif state == 'C':
        return 'D' if x == '0' else state
    elif state == 'D':
        return 'B' if x == '0' else 'E'
    elif state == 'E':
        return 'F' if x == '0' else state
    elif state == 'F':
        return 'E' if x == '1' else state
    elif state == 'G':
        return 'H' if x == '0' else state
    elif state == 'H':
        return 'J' if x == '0' else 'I'
    elif state == 'I':
        return 'K' if x == '0' else state
    elif state == 'J':
        return 'G' if x == '1' else state
    else:
        return 'I' if x == '1' else state