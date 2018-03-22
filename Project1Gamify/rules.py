'''
• The user starts out with 0 health points, and 0 hedons.
CHECK

• The user is always either running, carrying textbooks, or resting.
CHECK

• Running gives 3 health points per minutes for up to 180 minutes of running resting or carrying
textbooks, and 1 health point per minute for every minute over 180 minutes that the user runs.
(Note that if the user runs for 90 minutes, then rests for 10 minutes, then runs for 110 minutes, the
user will get 600 health points, since they rested in between the times that they ran.)
CHECK

• Carrying textbooks always gives 2 health points per minute.
CHECK

• Resting gives 0 hedons per minute.
CHECK

• Both running and carrying textbooks give -2 hedons per minute if the user is tired (definition: the
user is tired if they finished carrying running or carrying textbooks less than 2 hours before the
current activity started.)
CHECK

• If the user is not tired, running gives 2 hedons per minute for the first 10 minutes of running, and -2
hedons per minute for every minute after the first 10.
CHECK

• If the user is not tired, carrying textbooks gives 1 hedon per minute for the first 20 minutes, and -1
hedon per minute for every minute after the first 20.
CHECK

• If a star is offered for a particular activity and the user takes the star right away, the user gets an
additional 3 hedons per minute for at most 10 minutes. (Note that the user only gets 3 hedons per
minute for the first activity they undertake, and do not get the hedons due to the star if they decide
to keep performing the activity:

offer_star("running")
perform_activity("running", 5) #gets extra hedons
perform_activity("running", 2) #no extra hedons
CHECK

• If three stars are offered within the span of 2 hours, the user loses interest, and will not get additional
hedons due to stars for the rest of the simulation.
CHECK
'''