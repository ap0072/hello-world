from turtle import*

def main() :
     dictionary=("white","green","green","white","white","orange","orange")
     pu()
     goto(-320,-195)
     width(70)
     for i in dictionary:
          color(i)
          down()
          fd(840)
          up()
          bk(840)
          lt(90)
          fd(66)
          rt(90)     
 
     writer=Turtle()
     writer.ht()
     writer.pencolor("black")
     writer.write("\n\n\n         PYTON - DICTIONARY ",align="center",font=("Areial",56,("italic","bold")))



p="A Professional dictionary made by CHALUVADI PRASANTH KUMAR and SYED SHARUKH cse department" 
print(p)
d="   \n          PYTHON: - ENGLISH:  - MINI: - DICTIONARY:\n       (student's most trusted dictionary)"
print(d)
print("\n             INTODUCTION:\n  This is an experiment project to get a details of different english words\n  Here we are pursuing the different kinds of meanings of a words\n  some kind of matter so we should pursing to get meet the requirement \n  That is power of cse ")
print("                      INDEX         ")
my_pages=["1:in this page we consists of alphabets in alphabetical order which shows the order like letter 'D' which represents a kind of dictionary which consists of alphabets  in order resembling manner"]
for x in my_pages:
     print(x)
print("A\nP  B  C  D  \nQ           E\nR              F\nS      c        G\nT     CSE        h\nU      E         i\nV               j\nW             k\nX           L\nY  O  N  M   \nZ      ")
t="yes"
I="index"
x=input("     wanna to go for next page\t\t\t\n")
if(x==t):
     print("\ncongratulations we are successfully entering into the to next page")
     y=input("\nwanna to see all the content of all the pages\n")
     if(y==t):
          print("Thank you for choosing this option")
          my_dict={"name":"it is a representation of a person","animal":"its a living organisms generally which lives in forest","king":"a man who rules the kingdom.ex:alexander","collage":"the place where all the teenage students will study","exercise":" the activites should be done for good health"}
          print(my_dict)
          t=my_dict.keys()
          print(t)
          count=0
          s=input("ENTER A word\n")
          for x in t:
               if(x==s):
                    print("\n the word you are searching is  found successflly\n")
                    print("so the meaning of this word is ",my_dict.get(x))
                    print("thank you sir")
                    count=count+1
          if(count==0):
               print("ele not")      
     else:
          print("you are only intrested in watching dictionary")
          print("  thank you")
          
else:
     print("hurray we are in same page")
if __name__== "__main__":
     main()
     mainloop()

  
   
  
  
  
  
  




