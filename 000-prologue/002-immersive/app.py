print("\
    one\
    two\
    three\
");

a = "\
    first\
        second\
            third"

b = "\
    sai-sho\
        ni-ban-me\
            dai-san"

c = """
one
two
three
"""

d = "## golden as GOLD ###";

e,f,g = "1","11","111"

print(a + "\n" + b);
print('---');
print(c);
print(len(b))
print(a.strip())
print(a.strip())
print(a.rstrip()) #remove right spaces
print(a.lstrip()) #remove left spaces
print("--")
print(d);
print(d.strip("#"));

#title capitalize zfill upper
print(d.title())
print(d.capitalize())
print(e)
print(f)
print(g)
print("--")
print(e.zfill(3))
print(f.zfill(3))
print(g.zfill(3))
print("==")
print(d.upper())