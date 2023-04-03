
import time
import sys
# Get current time in milliseconds
now = int(time.time() * 1000)

# Add a month's worth of seconds
one_month_in_seconds = 31 * 24 * 60 * 60
one_month_from_now = int((time.time() + one_month_in_seconds) * 1000)

print(f"Now: {now}")
print(f"One month from now: {one_month_from_now}")


if now > one_month_from_now:
    sys.exit()

