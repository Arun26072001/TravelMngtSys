import pywhatkit
try:
    pywhatkit.sendwhatmsg(phone_no='+919361393856',message="Mama!!",time_hour=11,time_min=5,wait_time=30)
    print("message deleverd successfully!")
except:
    print("have error in this file!")
    