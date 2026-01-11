import datetime

utc_time = datetime.datetime.now(datetime.UTC)
print(utc_time)  # Результат будет в формате: YYYY-MM-DD HH:MM:SS.ss

current_datetime = datetime.datetime.now()
print(current_datetime)  # YYYY-MM-DD HH:MM:SS.ss
print(current_datetime.isoformat())  # YYYY-MM-DDTHH:MM:SS.ss
print(current_datetime.year)  # YYYY
print(current_datetime.month)  # MM
print(current_datetime.day)  # DD
print(current_datetime.hour)  # HH
print(current_datetime.minute)  # MM
print(current_datetime.second)  # SS
print(current_datetime.microsecond)  # ss

some_datetime = datetime.datetime(year=2021, month=5, day=1, hour=12, minute=30, second=15, microsecond=123456)
print(some_datetime)  # YYYY-MM-DD HH:MM:SS.ss

current_date = datetime.date.today()
print(current_date)  # YYYY-MM-DD

current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
print(current_date)  # YYYY-MM-DD


day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)  # YYYY-MM-DD HH:MM:SS.ss


current_datetime = datetime.datetime.now()
current_datetime.strftime("%A, %d %B %Y")  # Output will be in the format: Monday, 01 March 2021

iso_format = "2023-08-07T20:15:30.384294"
my_datetime = datetime.datetime.fromisoformat(iso_format)
print(type(my_datetime))  # <class 'datetime.datetime'>
print(my_datetime)  # 2023-08-07 20:15:30.384294
