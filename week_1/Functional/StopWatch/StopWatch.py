"""
Desc ­> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks

I/P ­> Start the Stopwatch and End the Stopwatch

Logic ­> Measure the elapsed time between start and end

O/P ­> Print the elapsed time
"""

import StopWatchBL as ob

# user input (Enter for start stop watch)
ready = int(input("Enter 1 if you want to start your stopwatch : "))

# print time from start to end
ob.startWatch(ready)
