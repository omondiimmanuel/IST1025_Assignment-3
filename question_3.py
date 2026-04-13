temp= []
#creating an empty list
for item in range(7):
#generating a sequence of days
    temperature= float(input(f"enter the temperature for day{item}:"))
    temp.append(temperature)
#calculating the temperature variables    
min_temp= min(temp)
max_temp= max(temp)
total_temp= sum(temp)
avg_temp = total_temp / len(temp)
#displaying the outputs
print(f"highest temp: {max_temp:.2f}")
print(f"lowest temp: {min_temp:.2f}")
print(f"sum of temperatures: {total_temp:.2f}")
print(f"average temperature: {avg_temp:.2f}")
