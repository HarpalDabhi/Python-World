# 1.
# A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?

speed=60 # km/h

new_speed=(60*1000)/3600 # or 60*(5/18) // m/s

print("%.2f"%new_speed,"m/s")

# v=m/t means m=v*t

t=9
v=new_speed

m=v*t
print(m)
