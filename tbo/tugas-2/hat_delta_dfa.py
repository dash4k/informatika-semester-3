from delta_dfa import l1_delta_dfa, l2_delta_dfa, l3_delta_dfa, l4_delta_dfa

def l1_hat_dfa(state, x) -> str:
    if x == '':
        return state
    else:
        return l1_delta_dfa(l1_hat_dfa(state, x[0:-1]), x[-1])

def l2_hat_dfa(state, x) -> str:
    if x == '':
        return state
    else:
        return l2_delta_dfa(l2_hat_dfa(state, x[0:-1]), x[-1])

def l3_hat_dfa(state, x) -> str:
    if x == '':
        return state
    else:
        return l3_delta_dfa(l3_hat_dfa(state, x[0:-1]), x[-1])

def l4_hat_dfa(state, x) -> str:
    if x == '':
        return state
    else:
        return l4_delta_dfa(l4_hat_dfa(state, x[0:-1]), x[-1])