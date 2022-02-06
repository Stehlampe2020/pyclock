try:
    version = "1.1"
    import time
    import sys
    
    args = sys.argv
    
    if (len(args) == 1) or ((len(args) == 2) and (args[1] == ("-n" or "--no-sync"))):
        hours, minutes, seconds = 00, 00, 00
        print(str(hours) + ":" + str(minutes) + ":" + str(seconds), end="\r")
        if len(args) == 2:
            if args[1] == ("-n" or "--no-sync"):
                secs_since_last_sync = 11
            else:
                secs_since_last_sync = 10
        else:
            secs_since_last_sync = 10

        while True:
            time.sleep(1)
            
            if secs_since_last_sync == 10:
                hours = round(float(time.strftime("%H")))
                minutes = round(float(time.strftime("%M")))
                seconds = round(float(time.strftime("%S")))
                secs_since_last_sync = 0
            elif secs_since_last_sync == 11:
                seconds += 1
            elif secs_since_last_sync < 10:
                seconds += 1
                secs_since_last_sync += 1

            if seconds == 60:
                minutes += 1
                seconds = 0
            elif minutes == 60:
                hours += 1
                minutes = 0
            elif hours == 24:
                hours = 0
                minutes = 0
                seconds = 0

            if hours <= 9:
                hours = "0" + str(hours)
            if minutes <= 9:
                minutes = "0" + str(minutes)
            if seconds <= 9:
                seconds = "0" + str(seconds)
            print(str(hours) + ":" + str(minutes) + ":" + str(seconds), end="\r")

            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)
    elif len(args) == 2 and args[-1] == "-i":
        print("PyClock version " + version + "\n\nUsage:\n-i              Show this info and exit.\n\nThis program was created by Christian Lampe <kontakt@lampe2020.de>.\n")
    
except KeyboardInterrupt:
    print("\rKeyboardInterrupt received at internal program time of " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds, exiting...")
