#split() rsplit()
s = "hello and welcome ..";
print(s.split());
print(s.rsplit());

ss = "hello-and-welcome ..";
print(ss.split());
print(ss.split("-"));

sss = "hello-and-welcome-and-have-a-good-time";
print(sss.split("-",2));

ssss = "hello-and-welcome-and-have-a-good-time";
print(ssss.rsplit("-",2));

#-------------------()

f = "fua";
print(f.rjust(10));
print(f.ljust(10, "#"));

v = """first line is
  seconds to the
  third Line
""";
print(v.splitlines())