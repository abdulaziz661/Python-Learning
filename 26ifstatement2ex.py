message = "The recpmmended activity is "
print ("Enter the tempratture: ")
temp = int(input())
if temp >85:
    message = message + "swimming."
elif temp >= 70:
    message = message + "tennis."
elif temp >= 32:
    message = message + "golf." 
elif temp >= 0:
    message = message + "sitting by the fire "
print (message)                   
