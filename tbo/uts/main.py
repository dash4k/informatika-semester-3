from nfa import nfa, delta_nfa


def test_nfa():
    test_cases = [
        (['succeed', '1', '1', 'exit', 'exit'], True),
        (['failed', 'failed', 'failed'], False),
        (['succeed', '2', '2', 'validate', 'exit', 'exit'], True),
        (['succeed', '3', '1', 'field_click', 'exit',], False),
        (['succeed', 'exit'], True),
        ([], False),
        (['failed', 'failed', 'failed', 'succeed', 'exit'], True),
    ]

    for i, (languages, expected) in enumerate(test_cases, 1):
        states = {'q0'}
        result = nfa(languages)
        print(f"Test Case {i}: {'Passed' if result == expected else 'Failed'}", end="")
        if result != expected:
            print(f"    Input: {languages}")
            print(f"    Expected: {expected}, Got: {result}")
        print(f" | States Transition: {states}", end="")
        for language in languages:
            curr = set()
            for state in states:
                curr = curr.union(delta_nfa(state, language))
            print(f" --> {curr}", end="")
            states = curr
        print()


test_nfa()