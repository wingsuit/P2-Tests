## Test Code ##
import time
def run_test(num, data, expected, explanation):
    start = time.time()
    output = str(build_cave(data))
    end = time.time()
    success = "PASSED" if output == expected else "FAIL"
    output = "Cave" if output != 'None' else output
    expected = "Cave" if expected != 'None' else expected
    print(f"{num:>3}{'|':>9}{output:>8}{'|':>9}{expected:>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  {explanation}")
    
def test():
    tests = [
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            "[['@', '.', 'W', '.'], ['.', '#', '#', '$'], ['.', 'X', '#', '#'], ['.', '.', '.', 't']]",
            "Example 1"
        ),
        (
            {'size': 4, 'entrance':(0, 0)},
            'None',
            "Example 2, no exit"
        ),
        (
            {'size': 4,'entrance': (0, 0),'exit': (4, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            "None",
            "Exit out of bounds"
        ),
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (4, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            "None",
            "Dragon out of bounds"
        ),
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 1), (1, 2), (1, 3), (2, 2)],'walls': [(2, 3)]},
            "None",
            "Too many treasures"
        ),
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 1),'sword': (3, 3),'treasure': [(1, 1), (1, 2), (1, 3)],'walls': [(2, 3)]},
            "None",
            "Dragon near entrance"
        )
    ]
    
    print(" Test #    |    Received    |    Expected    |    PASS/FAIL    |    Time     |    Test Type")
    print("-----------------------------------------------------------------------------------------------------")
    num = 1
    for data, expected, explanation in tests:
        run_test(num, data, expected, explanation)
        num += 1
        
test()
## Test Code ##
