import datetime
import time

epoch_time = time.time()
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} \
      or {epoch_time:2e} in scientific notation")

curr_time = datetime.datetime.now()
print(f"{curr_time.strftime('%b')} {curr_time.day} {curr_time.year}")
