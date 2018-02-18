#f=open("text.txt","w")
#f.write("hi! I am Mayank\n")
#f.write("I am a Roboticist\n")
#f.write("I am from Karnal\n")
#f.write("I like MS Dhoni\n")
#f.write("I love Python\n")


f=open("text.txt","a")
f.write("1")


f.close()
with open("text.txt","r") as f:
    print(f.read())