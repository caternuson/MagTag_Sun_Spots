import time
from adafruit_magtag.magtag import MagTag

URL = "https://raw.githubusercontent.com/caternuson/MagTag_Sun_Spots/main/out.bmp"
BMP = "out.bmp"

magtag = MagTag()

# connect to wifi and set time
magtag.get_local_time()

# helper for setting sleep time
def go_to_sleep():
    """Enter deep sleep for time needed."""
    # compute current time offset in seconds
    hour, minutes, seconds = time.localtime()[3:6]
    seconds_since_midnight = 60 * (hour * 60 + minutes) + seconds
    three_fifteen = (3 * 60 + 15) * 60
    # wake up 15 minutes after 3am
    seconds_to_sleep = (24 * 60 * 60 - seconds_since_midnight) + three_fifteen
    print(
        "Sleeping for {} hours, {} minutes".format(
            seconds_to_sleep // 3600, (seconds_to_sleep // 60) % 60
        )
    )
    magtag.exit_and_deep_sleep(seconds_to_sleep)


# ===========
#  M A I N
# ===========
print("Downloading BMP...")
magtag.network.wget(URL, BMP)

print("Setting background...")
magtag.set_background(BMP)

print("Adding time stamp...")
magtag.add_text(text_position=(2, 120))
magtag.set_text(magtag.get_local_time())

print("Sleeping...")
go_to_sleep()