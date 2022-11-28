import datetime
import time

def weekrange(p_year, p_week, dateform):

    firstday = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastday = firstday + datetime.timedelta(days=6.9)
    
    firstday = firstday.strftime(dateform)    
    lastday = lastday.strftime(dateform)

    return firstday, lastday

weeklist = {}

for i in range(2,54):
    weeklist.update({"Week " + str(i-1): weekrange("2023", i, "%B %d")})

print(weeklist)
