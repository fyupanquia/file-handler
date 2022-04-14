import time
from datetime import datetime as dt

hosts = "hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","www.youtube.com","www.instagram.com"]
START_WORKING_HOUR = 17
END_WORKING_HOUR = 18
while True:
    now = dt.now()
    if dt(now.year, now.month, now.day,START_WORKING_HOUR) < now < dt(now.year, now.month,now.day,END_WORKING_HOUR):
        with open(hosts,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website} \n")
    else:
        with open(hosts, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)