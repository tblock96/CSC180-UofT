### TESTING FOR gamify.py ###
from gamify import *

if __name__ == '__main__':
    '''Insert test cases here'''
    
    print("Begin testing.\n")
    '''Testing is done by evaluating all the rules in an order that makes sense.
    '''
    
    ## Test Case 1 ##
    '''The user starts out with 0 health points, and 0 hedons.'''
    initialize()
    if get_cur_hedons() != 0\
    and get_cur_health() != 0:   # Check health and hedons
        print("Test 1 failed!")                     # immediately after init.
    
    ## Test Case 2 ##
    '''The user is always either running, carrying textbooks, or resting.'''
    initialize()                                # Try performing an activity not
    perform_activity("something else", 20)      # listed and see if any time
    if get_cur_time() != 0:                     # passes.
        print("Test 2 failed!")

    ## Test Case 3 ##
    '''Running gives 3 health points per minutes for up to 180 minutes of
    running resting or carrying textbooks, and 1 health point per minute for
    every minute over 180 minutes that the user runs. (Note that if the user
    runs for 90 minutes, then rests for 10 minutes, then runs for 110 minutes,
    theuser will get 600 health points, since they rested in between the times
    that they ran.)'''
    initialize()                                # Make sure running gives 3 hp
    perform_activity("running", 180)            # for up to 180 minutes . . .
    if get_cur_health() != 180 * 3:             
        print("Test 3a failed!")
    perform_activity("running", 20)
    if get_cur_health() != 180 * 3 + 20:        # and then only 1 hp after that.
        print("Test 3b failed!")     
    perform_activity("resting", 1)              # Make sure that resting resets
    perform_activity("running", 10)             # running HP back to 3/min.
    if get_cur_health() != 190 * 3 + 20:
        print("Test 3c failed!")
        
    initialize()
    perform_activity("running", 180)
    perform_activity("textbooks", 1)            # Make sure that textbooks also
    perform_activity("running", 10)             # resets running HP back to 3.
    if get_cur_health() != 190 * 3 + 2:
        print("Test 3d failed!")
    
    initialize()
    perform_activity("running", 200)            # Make sure that performing >180
    if get_cur_health() != 180 * 3 + 20:        # mins of running in one
        print("Test 3e failed!")                # activity still works.

    ## Test Case 4 ##
    '''Carrying textbooks always gives 2 health points per minute.'''
    initialize()
    perform_activity("textbooks", 1)
    if get_cur_health() != 2:
        print("Test 4a failed!")                # Make sure textbooks give 2 HP.
    perform_activity("textbooks", 999)
    if get_cur_health() != 2 * 1000:            # Make sure length doesn't
        print("Test 4b failed!")                # affect HP given.

    ## Test Case 5 ##
    '''Resting gives 0 hedons per minute.'''
    initialize()
    perform_activity("resting", 10)             # Make sure resting gives no
    if get_cur_hedons() != 0:                   # hedons.
        print("Test 5 failed!")
    
    ## Test Case 6 ##
    '''If the user is not tired, running gives 2 hedons per minute for the first
    10 minutes of running, and -2 hedons per minute for every minute after the
    first 10.'''
    initialize()                                # Make sure user is not tired
    perform_activity("running", 10)             # Make sure user gets 2 hedons
    if get_cur_hedons() != 10 * 2:              # For full 10 minutes of
        print("Test 6a failed!")                # running.
    
    initialize()
    perform_activity("running", 15)             # Test for longer than 10 min
    if get_cur_hedons() != 10 * 2 - 5 * 2:      # of activity.
        print("Test 6b failed!")

    ## Test Case 7 ##
    '''If the user is not tired, carrying textbooks gives 1 hedon per minute for
    the first 20 minutes, and -1 hedon per minute for every minute after the
    first 20.'''
    initialize()                                # Make sure user is not tired
    perform_activity("textbooks", 20)           # Make sure user gets 1 hedons
    if get_cur_hedons() != 20:                  # For full 20 minutes of
        print("Test 7a failed!")                # textbooks.
    
    initialize()
    perform_activity("textbooks", 25)           # Test for longer than 20 min
    if get_cur_hedons() != 20 - 5:              # of activity.
        print("Test 7b failed!")
    
    ## Test Case 8 ##
    '''Both running and carrying textbooks give -2 hedons per minute if the user
    is tired (definition: the user is tired if they finished carrying running or
    carrying textbooks less than 2 hours before the current
    activity started.)'''
    initialize()                                # Test cases for each run/text
    perform_activity("running", 1)              # combination.
    perform_activity("running", 100)
    if get_cur_hedons() != 1 * 2 - 100 * 2:     # Also test that tiredness
        print("Test 8a failed!")                # overrules the length of
                                                # the activity.
    initialize()
    perform_activity("running", 1)
    perform_activity("textbooks", 10)
    if get_cur_hedons() != 1 * 2 - 10 * 2:
        print("Test 8b failed!")
    
    initialize()
    perform_activity("textbooks", 1)
    perform_activity("running", 2)
    if get_cur_hedons() != 1 - 2 * 2:
        print("Test 8c failed!")

    initialize()
    perform_activity("textbooks", 1)            # Also test that tiredness
    perform_activity("textbooks", 1000)         # overrules the length of the
    if get_cur_hedons() != 1 - 1000 * 2:        # activity.
        print("Test 8d failed!")
        
    initialize()
    perform_activity("running", 1)              # Test that resting resets
    perform_activity("resting", 200)            # tiredness.
    perform_activity("running", 10)
    if get_cur_hedons() != 1 * 2 + 10 * 2:
        print("Test 8e failed!")

    ## Test Case 9 ##
    '''If a star is offered for a particular activity and the user takes the
    star right away, the user gets an additional 3 hedons per minute for at most
    10 minutes. (Note that the user only gets 3 hedons per minute for the first
    activity they undertake, and do not get the hedons due to the star if they
    decide to keep performing the activity'''
    initialize()
    offer_star("running")                       # Test that stars increase
    perform_activity("running", 10)             # hedons per minute.
    if get_cur_hedons() != 10 * (2 + 3):
        print("Test 9a failed!")
    
    initialize()                                # Test that tiredness and stars
    perform_activity("running", 1)              # are compatible.
    offer_star("running")
    perform_activity("running", 10)
    if get_cur_hedons() != 2 + 10 * (3 - 2):
        print("Test 9b failed!")
    
    initialize()                                # Test that stars run out
    offer_star("running")                       # and that they don't affect
    perform_activity("running", 20)             # tests 6 & 7.
    if get_cur_hedons() != 10 * (3 + 2) - 10 * 2:
        print("Test 9c failed!")
    
    initialize()
    offer_star("textbooks")                     # Test that the user can reject
    perform_activity("running", 1)              # a star by performing a
    perform_activity("textbooks", 10)           # different activity.
    if get_cur_hedons() != 2 - 10 * 2:
        print("Test 9d failed!")
    
    initialize()                                # Test that the star only
    offer_star("textbooks")                     # applies to the first activity
    perform_activity("textbooks", 5)            # after the star is offered.
    perform_activity("textbooks", 5)
    if get_cur_hedons() != 5 * (3 + 1) - 5 * 2:
        print("Test 9e failed!")

    ## Test Case 10 ##
    '''If three stars are offered within the span of 2 hours, the user loses
    interest, and will not get additional hedons due to stars for the rest of
    the simulation.'''
    initialize()
    offer_star("running")                       # Test that the third star in
    perform_activity("running", 10)             # two hours has no effect.
    offer_star("textbooks")
    perform_activity("textbooks", 10)
    offer_star("running")
    perform_activity("running", 10)
    if get_cur_hedons() != 10 * (2 + 3) + 10 * (-2 + 3) - 10 * 2:
        print("Test 10a failed!")
    
    initialize()
    offer_star("running")                       # Test that if stars are offered
    offer_star("asdf")                          # at the same time the two-hour
    offer_star("textbooks")                     # rule still apllies, and that
    perform_activity("textbooks", 10)           # rejected stars still count
    if get_cur_hedons() != 10:                  # towards the two-hour rule.
        print("Test 10b failed!")               # Also test that all stars bore
                                                # the user.
    initialize()
    offer_star("textbooks")                     # Test that stars offered more
    perform_activity("textbooks", 120)          # than two hours apart do not
    offer_star("asdf")                          # make the user bored.
    offer_star("running")
    perform_activity("running", 10)
    if get_cur_hedons() != 10 * (3 + 1) + 10 - 100 + 10 * (3 - 2):
        print("Test 10c failed!")
    
    initialize()
    offer_star("asdf")
    offer_star("running")                       # Test that the user's boredom
    offer_star("textbooks")                     # lasts for the whole simulation
    perform_activity("resting", 120)            # even after 120 minutes from
    offer_star("running")                       # when it started.
    perform_activity("running", 10)
    if get_cur_hedons() != 10 * 2:
        print("Test 10d failed!")
    
    ## Edge Cases ## Not necessary for the project, but more satisfying to me.
    '''Performing an activity for zero minutes should not make the user
    tired, or do anything at all.'''
    initialize()
    perform_activity("running", 0)              # Test that the user doesn't get
    perform_activity("running", 10)             # tired from a 0 min activity.
    if get_cur_hedons() != 10 * 2:
        print("Test 11a failed!")
    
    initialize()
    offer_star("running")                       # Test that the user doesn't
    perform_activity("textbooks", 0)            # reject a star with a 0 minute
    perform_activity("running", 10)             # activity.
    if get_cur_hedons() != 10 * (2 + 3):
        print("Test 11b failed!")
    
    initialize()
    perform_activity("running", 180)            # Test that resting for 0 min
    perform_activity("resting", 0)              # does not count towards test 3.
    perform_activity("running", 20)
    if get_cur_health() != 180 * 3 + 20:
        print("Test 11c failed!")
    
    '''Performing an unspecified activity (like "asdf") should not make the user
    tired, or do anything at all.'''
    initialize()
    perform_activity("asdf", 10)                # Test that the user doesn't get
    perform_activity("running", 10)             # tired from an unspecified
    if get_cur_hedons() != 10 * 2:              # activity.
        print("Test 12a failed!")
    
    initialize()
    offer_star("running")                       # Test that the user doesn't
    perform_activity("asdf", 10)                # reject a star with an
    perform_activity("running", 10)             # unspecified activity.
    if get_cur_hedons() != 10 * (2 + 3):
        print("Test 12b failed!")

    initialize()
    perform_activity("running", 180)            # Test that performing an
    perform_activity("asdf", 10)                # uspecified activity does not
    perform_activity("running", 20)             # count towards test 3.
    if get_cur_health() != 180 * 3 + 20:
        print("Test 12c failed!")
    
    ## Test Case 13 ## Testing most_fun_activity_minute()
    '''most_fun_activity_minute() should return the activity that would give
    the most hedons if performed for one minute at that point in the simulation.
    ''' 
    initialize()
    if most_fun_activity_minute() != "running": # Test that running is the most
        print("Test 13a failed!")               # fun at the beginning.
    perform_activity("running", 10)
    if most_fun_activity_minute() != "resting": # Test that resting is the most 
        print("Test 13b failed!")               # fun when the user is tired.
    
    initialize()
    perform_activity("textbooks", 1)            # Test that stars affect the
    offer_star("textbooks")                     # fun activity.
    if most_fun_activity_minute() != "textbooks":
        print("Test 13c failed!")
    perform_activity("resting", 121)            # Test that resting until the
    if most_fun_activity_minute() != "running": # user isn't tired resets the 
        print("Test 13d failed!")               # most fun activity.
    perform_activity("textbooks", 1)
    if most_fun_activity_minute() != "resting": # Test that being tired after
        print("Test 13e failed!")               # resting maintains its normal
                                                # function.
    
    print("Testing complete. Failed tests are listed above.")