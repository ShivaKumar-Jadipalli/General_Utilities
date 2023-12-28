import datetime , pandas as pd ,plotly.express as px , win32evtlog 
hand = win32evtlog.OpenEventLog(None, "Security")
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
get_events = True    
total_time =[]
while get_events:
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    for event in events:
        event_time = event.TimeGenerated
        if str(event_time).startswith(str(datetime.datetime.now()).split(' ')[0]):
            total_time.append(event_time)
        else:
            get_events = False  
win32evtlog.CloseEventLog(hand)

waking_hours  = datetime.datetime.strptime("16:45:54", "%H:%M:%S")

today_date = total_time[-1].date()
previous_time = total_time[-1]
total_data = {"Hours":[],"Minutes":[],"Seconds":[],"Total_Minutes":[],"Started_on":[],"Ended_on":[],"Date":[]}
for present_time in total_time[::-1]:
    if present_time > previous_time:
        time_wasted = present_time - previous_time
        hours, remainder = divmod(time_wasted.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes > 10:
            total_data["Date"].append(today_date)
            total_data["Total_Minutes"].append(int(time_wasted.total_seconds()/60))
            total_data["Hours"].append(hours)
            total_data["Minutes"].append(minutes)
            total_data["Seconds"].append(seconds)
            total_data["Ended_on"].append(present_time.time())
            total_data["Started_on"].append(previous_time.time())
        previous_time = present_time
total_data_dataframe = pd.DataFrame(total_data)
hours, remaining_minutes = divmod(sum(total_data_dataframe['Total_Minutes']), 60)
time_stamp = datetime.datetime.strptime("{:02d}:{:02d}:00".format(hours, remaining_minutes), "%H:%M:%S")

time_wasted_overall = waking_hours - time_stamp

fig = px.bar(total_data_dataframe,y='Total_Minutes',hover_data=["Started_on","Ended_on"],title=f"Total time wasted on {today_date}",color_discrete_sequence=['green'])
fig.update_layout(
    xaxis_title=f"Total time wasted {time_wasted_overall}", yaxis_title="Total Minutes "
)
print(fig.show())