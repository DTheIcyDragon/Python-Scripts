def sec_to_min(time: int):
    hours, seconds = divmod(time, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return str(hours) + "h " + str(minutes) + "m " + str(int(seconds)) + "s"
