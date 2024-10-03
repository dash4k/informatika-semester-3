from delta_dfa import l1_delta, l2_delta, l3_delta, l4_delta

def l1_hat(state, x) -> str:
    if x == '':
        return state
    else:
        state = l1_delta(l1_hat(state, x[0:-1]), x[-1])
        print(f"--> {state} ", end='')
        return state

def l2_hat(state, x) -> str:
    if x == '':
        return state
    else:
        state = l2_delta(l2_hat(state, x[0:-1]), x[-1])
        print(f"--> {state} ", end='')
        return state

def l3_hat(state, x) -> str:
    if x == '':
        return state
    else:
        state = l3_delta(l3_hat(state, x[0:-1]), x[-1])
        print(f"--> {state} ", end='')
        return state

def l4_hat(state, x) -> str:
    if x == '':
        return state
    else:
        state = l4_delta(l4_hat(state, x[0:-1]), x[-1])
        print(f"--> {state} ", end='')
        return state