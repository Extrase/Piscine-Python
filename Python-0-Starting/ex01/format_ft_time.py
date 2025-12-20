import time
import datetime

t = time.time()

myDate = datetime.date.today()
p = myDate.strftime("%b %w %Y")
print(f"Seconds since January 1, 1970: {t:,.4f} or {t:.2e} in scientific notation")
print(f"{p}")