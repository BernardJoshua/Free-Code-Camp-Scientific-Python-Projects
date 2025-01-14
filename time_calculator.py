def add_time(start, duration, day=None):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Parse the start time (hour, minute, AM/PM)
    hour = int(start.split(':')[0])
    minute = int(start.split(':')[1].split(' ')[0])
    time_frame = start.split(' ')[1]  # AM or PM

    # Parse the duration time (hours and minutes)
    hours = int(duration.split(':')[0])
    mins = int(duration.split(':')[1])

    # Calculate the total hours and minutes
    hour += hours
    minute += mins

    # Adjust minutes and carry over to hours if necessary
    if minute >= 60:
        minute -= 60
        hour += 1

    # Calculate total days and remaining hours
    total_days = hour // 24 + 1
    hour %= 24

    # Determine the day if provided
    if day is not None:
        day = day.strip().capitalize()  # Normalize the day string (case-insensitive)
        start_day_index = days_of_week.index(day)
        new_day_index = (start_day_index + total_days) % 7
        new_day = days_of_week[new_day_index]

    # Adjust for 12-hour format and AM/PM
    if hour == 0:
        hour = 12
        time_frame = "AM"
    elif hour > 12:
        hour -= 12
        time_frame = "PM" if time_frame == "AM" else "AM"
    elif hour == 12:
        time_frame = "PM"  # Keep it as PM if it's exactly 12 noon or midnight

    # Flip AM/PM for every 12 hours added
    total_flips = (hours + (minute // 60)) // 12
    if total_flips % 2 == 1:
        time_frame = "PM" if time_frame == "AM" else "AM"

    # Formulate the output with correct day and time
    if total_days == 1:
        next_day = ""
    elif total_days == 2:
        next_day = "(next day)"
    else:
        next_day = f"({total_days} days later)"

    # If day is provided, include it in the result
    if day is not None:
        time = f"{hour}:{minute:02d} {time_frame}, {new_day} {next_day}"
    else:
        time = f"{hour}:{minute:02d} {time_frame} {next_day}"

    # Return the result
    return time
