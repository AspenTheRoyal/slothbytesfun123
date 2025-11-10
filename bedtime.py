from datetime import datetime, timedelta

def bedTime(*listoftimes):
    for times in listoftimes:
        alarmtime = datetime(2025,2,2,int(times[0][:2]),int(times[0][3:]),0,0)
        subtractiontime = timedelta(hours=int(times[1][:2]),minutes=int(times[1][3:]))
        bedtimesolution = alarmtime - subtractiontime
        print(bedtimesolution.strftime("%H:%M"))

bedTime(["07:50", "07:50"])
#output = ["00:00"]

bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"])
#output = ["20:15", "22:00", "23:30"]


bedTime(["05:45", "04:00"], ["07:10", "04:30"])
#output = ["01:45", "02:40"]
