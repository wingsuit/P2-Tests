from Q3 import shortest_path
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
        )
    ]

    ##Test
    
    print(" Test #    |    Received    |    Expected    |    PASS/FAIL    |    Time     |    Test Type")
    print("-----------------------------------------------------------------------------------------------------")
    num = 1
    for data, ent, ex, sword, expected, explanation in tests:
        run_test(num, data, ent, ex, sword, expected, explanation)
        num += 1

test()
