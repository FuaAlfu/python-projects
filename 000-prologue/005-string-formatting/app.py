name = "name"
age = 9999
rank = 999

#old
print("my Name is: " + name);
#print("my Name is: " + name + "my age is:" + age);

print("my Name is %s" % "name")
print("my Name is %s" % name)
print("my Name is: %s and my AGE is: %s" % (name, age))

#modern
print("---")
print("my Name is: {}".format(name))
print("my Name is: {} and my AGE is: {}".format(name, age))
print("my Name is: {}, my Rank is: {} and my AGE is: {}".format(name, age,rank))
print("my Name is: {:s}, my Rank is: {:d} and my AGE is: {:f}".format(name, age,rank))

