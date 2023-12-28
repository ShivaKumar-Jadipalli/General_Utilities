import datetime , pandas as pd ,plotly.express as px 
today_date = datetime.datetime.now()
file_path = r"D:\New_Journey\Coding\OdinSchool_questions\System_Usage_time\output.txt"
with open(file_path, 'r', encoding='utf-16') as file:
    time_stamps = [line.strip() for line in file]
given_time = []
for time_string in time_stamps:
    time_object = datetime.datetime.strptime(time_string, "%H:%M:%S")
    given_time.append(time_object)
previous_time = given_time[-1]
total_data = {"Hours":[],"Minutes":[],"Seconds":[],"Total_Minutes":[],"Started_on":[],"Ended_on":[]}
for present_time in given_time[::-1]:
    if present_time > previous_time:
        time_wasted = present_time - previous_time
        hours, remainder = divmod(time_wasted.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes > 10:
            total_data["Total_Minutes"].append(int(time_wasted.total_seconds()/60))
            total_data["Hours"].append(hours)
            total_data["Minutes"].append(minutes)
            total_data["Seconds"].append(seconds)
            total_data["Ended_on"].append(present_time)
            total_data["Started_on"].append(previous_time)
        previous_time = present_time
total_data_dataframe = pd.DataFrame(total_data)
print(px.bar(total_data_dataframe,y='Total_Minutes',hover_data=["Started_on","Ended_on"],title=f"Total time wasted on {today_date}").show())