import time


def run_test(num, data, ent, ex, sword, expected, explanation):
    start = time.time()
    output = str(shortest_path(data, ent, ex, sword))
    end = time.time()
    success = "PASSED" if output == expected else "FAIL"
    print(f"{num:>3}{'|':>9}{output:>8}{'|':>9}{expected:>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  {explanation}")


def test():
    tests = [
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            (0, 0),
            (3, 3),
            False,
            '6',
            "Example 1",
        ),
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            (0, 0),
            (1, 3),
            False,
            'None',
            "Example 2",
        ),
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            (0, 0),
            (1, 3),
            True,
            '4',
            "Example 2 but with sword",
        ),(
            {'size': 5, 'entrance': (0, 2), 'exit': (0, 4), 'dragon': (2, 1), 'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            (0, 0),
            (4, 0),
            False,
            '12',
            "Have to walk the entire outside of the cave"
        ),(
            {'size': 5, 'entrance': (0, 2), 'exit': (0, 4), 'dragon': (2, 1), 'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            (0, 0),
            (4, 0),
            True,
            '6',
            "The same but this time we have a sword"
        ),(
            {'size': 5, 'entrance': (0, 2), 'exit': (4, 4), 'sword': (0, 0), 'dragon': (2, 1),
             'treasure': [(0, 3), (4, 1)], 'walls': [(4, 3), (1, 3), (2, 3), (3, 3)]},
            (0, 0),
            (4, 4),
            False,
            '8',
            "Right then down"
        ),(
            {'size': 5, 'entrance': (0, 2), 'exit': (4, 4), 'sword': (0, 0), 'dragon': (2, 1),
             'treasure': [(0, 3), (4, 1)], 'walls': [(4, 3), (1, 3), (2, 3), (3, 3)]},
            (0, 0),
            (4, 4),
            False,
            '8',
            "The same but holding a sword, dragon but not a shorter path)"
        ),(
            {'size': 5, 'entrance': (0, 2), 'exit': (4, 4), 'sword': (0, 0), 'dragon': (2, 1),
             'treasure': [(0, 3), (4, 1)], 'walls': [(4, 3), (1, 3), (2, 3), (3, 3)]},
            (4, 0),
            (4, 4),
            False,
            'None',
            "Dragon is blocking the way"
        ),(
            {'size': 5, 'entrance': (0, 2), 'exit': (4, 4), 'dragon': (0, 4),
             'walls': [(3, 1), (3, 2), (1, 3), (2, 3), (3, 3)]},
            (0, 2),
            (4, 4),
            True,
            '6',
            "Shorter through dragon, with sword"
        ),(
            {'size': 5, 'entrance': (0, 2), 'exit': (4, 4), 'dragon': (0, 4),
             'walls': [(3, 1), (3, 2), (1, 3), (2, 3), (3, 3)]},
            (0, 2),
            (4, 4),
            False,
            '10',
            "Shorter through dragon, without sword"
        )
    ]

    print(" Test #    |    Received    |    Expected    |    PASS/FAIL    |    Time     |    Test Type")
    print("-----------------------------------------------------------------------------------------------------")
    num = 1
    for data, ent, ex, sword, expected, explanation in tests:
        run_test(num, data, ent, ex, sword, expected, explanation)
        num += 1

test()
