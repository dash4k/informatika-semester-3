def delta_nfa(state, language):
    transition = {
        ('q0', 'succeed'): {'q1'},
        ('q0', 'failed'): {'q0'},
        ('q1', '1'): {'q2'},
        ('q1', '2'): {'q3'},
        ('q1', '3'): {'q4'},
        ('q1', 'exit'): {'q17'},
        ('q2', '1'): {'q5'},
        ('q2', '2'): {'q6'},
        ('q3', '1'): {'q7'},
        ('q3', '2'): {'q8'},
        ('q4', '1'): {'q9'},
        ('q4', '2'): {'q10'},
        ('q5', 'field_click'): {'q11'},
        ('q5', 'exit'): {'q1'},
        ('q6', 'validate'): {'q12'},
        ('q6', 'exit'): {'q1'},
        ('q7', 'field_click'): {'q13'},
        ('q7', 'exit'): {'q1'},
        ('q8', 'validate'): {'q14'},
        ('q8', 'exit'): {'q1'},
        ('q9', 'field_click'): {'q15'},
        ('q9', 'exit'): {'q1'},
        ('q10', 'validate'): {'q16'},
        ('q10', 'exit'): {'q1'},
        ('q11', 'exit'): {'q5'},
        ('q12', 'exit'): {'q1'},
        ('q13', 'exit'): {'q7'},
        ('q14', 'exit'): {'q1'},
        ('q15', 'exit'): {'q9'},
        ('q16', 'exit'): {'q1'},
    }
    return transition.get((state, language), set())


def hat_delta_nfa(states, languages):
    for language in languages:
        curr = set()
        for state in states:
            curr = curr.union(delta_nfa(state, language))
        states = curr
    return states


def nfa(languages):
    return True if {'q17'}.intersection(hat_delta_nfa({'q0'}, languages)) != set() else False