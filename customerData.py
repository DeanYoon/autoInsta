import datetime
# Create a datetime object for April 1, 2023 at 12:00 AM
start_date = datetime.datetime(2023, 4, 7, 0, 0)
# start_date = datetime.datetime.now()

# Add one month to the datetime object
expiry_date = start_date + datetime.timedelta(days=31)
CLIENT_SERIAL_NUMBER = 'GFQJL7CJW9'
get_serial_only = False


remaining_time = expiry_date - datetime.datetime.now()
print(remaining_time.total_seconds)
print(type(remaining_time.total_seconds()))


