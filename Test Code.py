def test_suite():
    
    print(" Test #    |    Recieved    |    Expected    |    PASS/FAIL    |    Time     |    Test Type")
    print("-----------------------------------------------------------------------------------------------------")
    
    #Example 1, expect 23
    data_example_1 = {'size': 4,'entrance': (0, 0),'exit': (2, 1),'dragon': (0, 2),'sword': (3, 3),'treasure': [(1, 3)],'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]}
    start = time.time()
    output = optimal_path(data_example_1)
    end = time.time()
    success = "PASSED" if output == 23 else "FAIL"
    print(f"{'1':>3}{'|':>9}{output:>8}{'|':>9}{'23':>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  First example")


    # Example 2, expect 14
    data_example_2 = {'size': 5,'entrance': (0, 2),'exit': (0, 4),'sword': (0, 0),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]}
    start = time.time()
    output = optimal_path(data_example_2)
    end = time.time()
    success = "PASSED" if output == 14 else "FAIL"
    print(f"{'2':>3}{'|':>9}{output:>8}{'|':>9}{'14':>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  Second example")
    
    # Example 3, expect None
    data_exit_unreachable = {'size': 5,'entrance': (0, 2),'exit': (4, 4),'sword': (0, 0),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(4,3),(3,4),(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]}
    start = time.time()
    output = optimal_path(data_exit_unreachable)
    end = time.time()
    success = "PASSED" if output == None else "FAIL"
    print(f"{'3':>3}{'|':>9}{str(output):>8}{'|':>9}{'None':>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  The exit is unreachable")
    
    # Example 4, expect 16
    data_no_sword = {'size': 5,'entrance': (0, 2),'exit': (0, 4),'dragon': (2, 1),'treasure': [(0, 3), (4, 1)],'walls': [(1, 0), (2, 0), (3, 0), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]}
    start = time.time()
    output = optimal_path(data_no_sword)
    end = time.time()
    success = "PASSED" if output == 16 else "FAIL"
    print(f"{'4':>3}{'|':>9}{str(output):>8}{'|':>9}{'16':>9}{'|':>8}{success:>11}{'|':>7}  {(end-start):.7f}{'|':>3}  There is no sword")
 
    
test_suite()
