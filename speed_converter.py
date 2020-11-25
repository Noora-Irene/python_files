print("KPH \t MPH")
print("--------------------")

for kph in range(60, 140, 10):
 mph = kph*0.621371
 if kph == 140:
  break
 print(kph, "\t", format(mph, ".1f"))