def convertTimeToStandard(time):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    return ("%02d:%02d" + setting) % (hours, minutes)