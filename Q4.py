import time
def run_test(num, data, expected, explanation):
    start = time.time()
    output = str(optimal_path(data))
    end = time.time()
    success = "PASSED" if output == expected else "FAIL"
    print(f"{num:>3}{'|':>9}{output:>8}{'|':>9}{'23':>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  First example")
    
def test():
    tests = [
        (
            {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]},
            "23",
            "Example 1"
        ),
        (
            {'size': 5,'entrance': (0, 2),'exit': (0, 4),'sword': (0, 0),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            "14",
            "Example 2"
        ),
        (
            {'size': 5,'entrance': (0, 2),'exit': (4, 4),'sword': (0, 0),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(4,3),(3,4),(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            'None',
            "Exit unreachable"
        ),
        (
            {'size': 5,'entrance': (0, 2),'exit': (0, 4),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]},
            '16',
            "No sword"
        )
    ]
    
    print(" Test #    |    Received    |    Expected    |    PASS/FAIL    |    Time     |    Test Type")
    print("-----------------------------------------------------------------------------------------------------")
    num = 1
    for data, expected, explanation in tests:
        run_test(num, data, expected, explanation)
        num += 1
        
test()
