import datetime

current_time=datetime.datetime.now()
print(current_time)

q=datetime.datetime.now()

print(q.strftime("%A"))

print(q.strftime("%a"))
print(q.strftime("%d"))
print(q.strftime("%b"))
print(q.strftime("%B"))
print(q.strftime("%y"))
print(q.strftime("%Y"))
print(q.strftime("%p"))