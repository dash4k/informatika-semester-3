from nfa import nfa


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
        result = nfa(languages)
        print(f"Test Case {i}: {'Passed' if result == expected else 'Failed'}")
        if result != expected:
            print(f"    Input: {languages}")
            print(f"    Expected: {expected}, Got: {result}")

test_nfa()