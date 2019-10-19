import time


def run_test(num, data, path, expected, explanation):

    start = time.time()
    output = str(check_path(data, path))
    end = time.time()
    success = "PASSED" if output == expected else "FAIL"
    print(f"{num:>3}{'|':>9}{output:>8}{'|':>9}{expected:>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  {explanation}")


def test():
    tests = [
        (
            {'size': 4, 'entrance': (0, 0), 'exit': (2, 1), 'dragon': (0, 2), 'sword': (3, 3), 'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            'True',
            (['S'] * 3 + ['E'] * 3 + ['W'] * 3 + ['N'] * 3 + ['E'] * 3 + ['S'] + ['N'] + ['W'] * 3 + ['S', 'S', 'E']),
            "Example 1"
        ),(
            {'size': 4, 'entrance': (0, 0), 'exit': (2, 1), 'dragon': (0, 2), 'sword': (3, 3), 'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            'False',
            (['S'] * 4),
            "Example 2"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (4, 4), 'sword' : (2, 2),'dragon': (0, 4),'walls': [(3, 1), (3, 2), (1, 3), (2, 3), (3, 3)]},
            'True',
            (['S'] * 2 + ['N'] * 2 + ['E'] * 2 + ['S'] * 4),
            "Grab sword then go through dragon and exit"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (4, 4), 'sword' : (2, 2),'dragon': (0, 4),'walls': [(3, 1), (3, 2), (1, 3), (2, 3), (3, 3)]},
            'False',
            (['E'] * 2 + ['S'] * 4),
            "Go through dragon and exit"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (4, 4), 'sword' : (2, 2),'treasure': [(0, 0)],'dragon': (0, 4),'walls': [(3, 1), (3, 2), (1, 3), (2, 3), (3, 3)]},
            'True',
            (['W'] * 2 + ['E'] * 2 + ['S'] * 2 + ['N'] * 2 + ['E'] * 2 + ['S'] * 4),
            "Grab treasure, then sword then go through dragon and exit"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (4, 4), 'sword' : (2, 2),'treasure': [(0, 0)],'dragon': (0, 4),'walls': [(3, 1), (3, 2), (1, 3), (2, 3), (3, 3)]},
            'False',
            (['S'] * 2 + ['N'] * 2 + ['E'] * 2 + ['S'] * 4),
            "Exited but didn't grab the treasure"
        )
    ]

    print(" Test #    |    Received    |    Expected    |    PASS/FAIL    |    Time     |    Test Type")
    print("-----------------------------------------------------------------------------------------------------")
    num = 1
    for data, expected, path, explanation in tests:
        run_test(num, data, path, expected, explanation)
        num += 1

test()