from datetime import datetime, time
from pytz import timezone

# Retrieve timezone from each city
Portland = timezone("US/Pacific")
NYC = timezone("US/Eastern")
London = timezone("Europe/London")

# Retrive current time from each city
p_time = datetime.now(Portland)
n_time = datetime.now(NYC)
l_time = datetime.now(London)

"""
This will print each time of each city:
print(p_time.strftime("%H:%M:%S"))
print(n_time.strftime("%H:%M:%S"))
print(l_time.strftime("%H:%M:%S"))
"""


def is_branch_open(begin_time, end_time, check_time=None):
    check_time = p_time.time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time

# Sets begin_time and end_time and then returns a boolean
print("Is the Portland branch open?", is_branch_open(time(9,0), time(17,0)))


# Portland = US/Pacific
# NYC = US/Eastern
# London = Europe/London
