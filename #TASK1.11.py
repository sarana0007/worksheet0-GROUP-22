#TASK1

#given temperatures
temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3, 13.4, 8.1,
17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7, 7.8, 17.5, 13.6, 8.7,
17.1, 13.8, 9.2, 18.1, 13.9, 8.3, 16.4, 12.7, 8.9, 18.2, 13.1, 7.8,
16.6, 12.5]

#create empty list for each category
cold = []
mild = []
comfortable = []

#classify each temperature
for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp < 20:
        comfortable.append(temp)

#print the outcomes
print("Cold : ", cold)
print("Mild : ", mild)
print("Comfortable : ", comfortable)

#TASK2

#count the number of items in each list
cold_count = len(cold)
mid_count = len(mild)
comfortable_count = len(comfortable)

#print the outcomes
print("cold count : ", cold_count)
print("mild count : ", mid_count)
print("comfortable count : ", comfortable_count)

#TASK3

#create new list for temp in fahrenheit
temperatures_fahrenheit = []

for temp in temperatures:
    fahrenheit = (temp * 9/5)+32
    temperatures_fahrenheit.append(fahrenheit)

print("temperautures in fahrenheit : ", temperatures_fahrenheit)

#TASK4

#create empty lists for each time of the day
night_temps = []
evening_temps = []
day_temps = []

#group the temperatures
for temp in range(0, len(temperatures), 3):
    night_temps.append(temperatures[temp])
    evening_temps.append(temperatures[temp+1])
    day_temps.append(temperatures[temp+2])

#calculate the average day time temperature
average_day_temp = sum(day_temps)/len(day_temps)

#print the required outputs
print("Night temperatures : ", night_temps)
print("Evening temperatures : ", evening_temps)
print("Day temperatures : ", day_temps)
print("Average day-time temperature : ",average_day_temp)

#plot "day vs temperature" using matplotib
"""
import matplotlib.pyplot as plt

#plot day-time temperatures
days = list(range(1, len(day_temps)+1))
plt.plot(days, day_temps, marker='o', color="red", label="Day Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature(°C)")
plt.title("Day vs Temperature")
plt.legend()
plt.show()
"""