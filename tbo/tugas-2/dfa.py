from hat_delta_dfa import l1_hat_dfa, l2_hat_dfa, l3_hat_dfa, l4_hat_dfa

def l1_dfa(x) -> bool:
    return True if l1_hat_dfa('A', x) == 'F' else False

def l2_dfa(x) -> bool:
    return True if l2_hat_dfa('A', x) == 'E' else False

def l3_dfa(x) -> bool:
    state = l3_hat_dfa('A', x)
    return True if  state == 'E' or state == 'C' else False

def l4_dfa(x) -> bool:
    state = l4_hat_dfa('A', x)
    return True if  state == 'F' or state == 'I' else False