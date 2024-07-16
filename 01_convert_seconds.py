def convert_sec(seconds):
    hrs = seconds // 3600
    min = (seconds - hrs * 3600) // 60
    sec = seconds - hrs * 3600 - min * 60
    return hrs, min, sec
hrs , min, sec = convert_sec(5000)
print(hrs , min, sec)