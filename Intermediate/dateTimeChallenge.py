# Utilize datetime to determine current time
from datetime import datetime
# Utilize the pytz package which provides the necessary timezone format to datetime
import pytz

# Determine the current local time in hours in Portland
pacific = pytz.timezone('America/Los_Angeles')
pacificNowFull = datetime.now(pacific)
pacificNowHour = int(pacificNowFull.strftime('%H'))

# Determine the current local time in hours in New York
newYork = pytz.timezone('America/New_York')
newYorkNowFull = datetime.now(newYork)
newYorkNowHour = int(newYorkNowFull.strftime('%H'))

# Determine the current local time in hours in London
london = pytz.timezone('Europe/London')
londonNowFull = datetime.now(london)
londonNowHour = int(londonNowFull.strftime('%H'))


# When called upon, determines if a passed time falls within the hours of 9:00AM to 5:00PM
def isOpen(localTime):
    if 9 <= localTime <= 16:
        return True


# When called upon, generates the output statement to display whether a company branch with a passed location and local
# time is open
def outputStatement(location, localTime):
    """Displays whether a company branch is open based upon the passed timezone location and the local current time"""
    if isOpen(localTime):
        print('The company branch based in the '+str(location)+' timezone is OPEN.')
    else:
        print('The company branch based in the '+str(location)+' timezone is CLOSED.')


# Pass the previously defined locations and each location's local time to the outputStatement function
outputStatement(pacific, pacificNowHour)
outputStatement(newYork, newYorkNowHour)
outputStatement(london, londonNowHour)










