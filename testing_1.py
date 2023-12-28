import win32evtlog
def get_user_session_log():
    hand = win32evtlog.OpenEventLog(None, "Security")
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    print(flags)
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    print(events)
    session_logs = []
    for event in events:
        event_id = event.EventID
        event_time = event.TimeGenerated
        print(event_id,event_time,task_category)
    win32evtlog.CloseEventLog(hand)
    return 0
if __name__ == "__main__":
    user_session_logs = get_user_session_log()
