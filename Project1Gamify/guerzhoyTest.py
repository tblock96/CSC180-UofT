def run_test(actual, expected):
    if expected == actual:
        return "passed"
    else:
        return "failed"

if __name__ == '__main__':
    import gamify
    
    gamify.initialize()
    
    gamify.perform_activity("textbooks", 2)    
    print("Test 1:", run_test(gamify.get_cur_health(), 4))
    print("Test 2:", run_test(gamify.get_cur_hedons(), 2))
    
    
    gamify.perform_activity("running", 5)    
    print("Test 3:", run_test(gamify.get_cur_health(), 19))
    print("Test 4:", run_test(gamify.get_cur_hedons(), -8))
    
    gamify.perform_activity("resting", 10)
    print("Test 5:", run_test(gamify.get_cur_health(), 19))
    print("Test 6:", run_test(gamify.get_cur_hedons(), -8))