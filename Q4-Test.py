import time

def run_test(num, data, expected, explanation):
    start = time.time()
    output = str(optimal_path(data))
    end = time.time()
    success = "PASSED" if output == expected else "FAIL"
    print(f"{num:>3}{'|':>9}{output:>8}{'|':>9}{expected:>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  {explanation}")

def test():
    tests = [
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            "23",
            "Example 1"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (0, 4),'sword': (0, 0),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            "14",
            "Example 2"
        ),(
            {'size': 4,'entrance': (0, 3),'exit': (3, 3),'sword': (0, 0),'dragon': (3, 2),'treasure': [(1, 3)]},
            "9",
            "Quicker to go sword first then treasure."
        ),(
            {'size': 4,'entrance': (0, 2),'exit': (3, 3),'treasure': [(0, 0), (0, 3), (1, 3)]},
            "8",
            "Quicker to go to furthest treasure first."
        ),(
            {'size': 5,'entrance': (1, 1),'exit': (4, 0), 'sword': (4, 4), 'dragon': (4,1), 'treasure': [(0, 1), (1, 0), (2, 1)], 'walls': [(1, 3), (2, 3), (3, 3), (4, 3)]},
            "22",
            "Complicated cave."
        ),(
            {'size': 5,'entrance': (1, 0),'exit': (4, 4),'sword': (4, 0),'dragon': (1, 2),'treasure': [(0, 0), (0, 4)]},
            '15',
            "Example from Tia"
        ),(
            {'size': 5,'entrance': (1, 0),'exit': (4, 4),'sword': (3, 0),'dragon': (1, 2),'treasure': [(0, 0), (0, 4)]},
            '13',
            "Updated example from Tia"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (4, 4),'sword': (0, 0),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(4,3),(3,4),(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            'None',
            "Exit unreachable"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (0, 4),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            '16',
            "No sword"
        ),(
            {'size': 6, 'entrance': (0, 1), 'exit': (0,5), 'dragon': (0, 3), 'sword': (0, 0)},
            '6',
            "No treasure or walls. Grab sword kill dragon exit"
        ),(
            {'size': 6, 'entrance': (0, 1), 'exit': (0,5), 'dragon': (0, 3)},
            '8',
            "No treasure, walls or sword. Walk around dragon"
        ),(
            {'size': 6, 'entrance': (5, 5), 'exit': (0,1)},
            '9',
            "Just entrance and exit"
        ),(
            {'size': 6, 'entrance': (0, 0), 'exit': (2, 2), 'walls': [(0, 1), (1, 1), (1, 0)]},
            'None',
            "Just entrance and exit, but exit unreachable"
        ),(
            {'size': 5,'entrance': (0, 2),'exit': (0, 4),'sword': (0, 0),'dragon': (2, 1),'treasure': [(0, 3), (3, 4)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            '8',
            "Quicker without the sword"
        )
    ]
    
    print(" Test #    |    Received    |    Expected    |    PASS/FAIL    |    Time     |    Test Type")
    print("-----------------------------------------------------------------------------------------------------")
    num = 1
    for cavem, expected, explanation in tests:
        run_test(num, cavem, expected, explanation)
        num += 1

test()
