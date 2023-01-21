# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

from datetime import datetime

print(f"{datetime(*kata).strftime('%m/%d/%Y %H:%M')}")
