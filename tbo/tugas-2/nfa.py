from hat_delta_nfa import l1_hat_nfa, l2_hat_nfa, l3_hat_nfa, l4_hat_nfa

def l1_nfa(x) -> bool:
    return True if {'E'}.intersection(l1_hat_nfa({'A'}, x)) != set() else False

def l2_nfa(x) -> bool:
    return True if {'E'}.intersection(l2_hat_nfa({'A'}, x)) != set() else False

def l3_nfa(x) -> bool:
    return True if  {'C', 'E'}.intersection(l3_hat_nfa({'A'}, x)) != set() else False

def l4_nfa(x) -> bool:
    return True if  {'F', 'I'}.intersection(l4_hat_nfa({'A'}, x)) != set() else False