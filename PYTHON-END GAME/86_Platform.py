import platform

a=platform.system()
print(a)

b=platform.architecture()
print(b)

c=platform.uname()
print(c)

d=platform.processor()
print(d)

e=platform
print(e)

import mymodule

print(mymodule.a["Name"])

print(mymodule.cube(5))

print(dir(platform))