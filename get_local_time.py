import datetime

def get_local_time_and_date():
    """Returns the current local time and date."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    print(get_local_time_and_date())
