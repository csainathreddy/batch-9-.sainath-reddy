 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# s1 = s1"Hello how are you"
# s2 = "Hello how is"

# s1 = s1.split("")
# s2 = s2.split("")

# for val in s1:
#   if val not in s2:
#       print(val)
#for val in s2:
#   if val not in s1:
#       print(val)

#3.)wrire a code print the fibanochi number
#0,1,1,2,3,5,8


n1 = 0
n2 = 1
# ans = 0+1 ==> 1

n1 = 1
n2 = 1
# ans = 1+1 ==> 2

n1 = 1
n2 = 2
# ans = 1+2==> 3

n1 = 2
n2 = 3
# ans = 2+3 ==> 5

# ! find the 8th fibanochi number
num = 8
n1 = 0
n2 = 1

for val in range(5):
    ans = n1+n2
    print(ans)
    n1 = n2
    n2 = ans
print(ans)

# ! constructors
# ? Eg:2
# * unparametarised constructor
class profile:
    def_ init_(self):
        print("hello world)

obj = profile()
obj._init)()

#?Eg:3
# * parametarised constructor
class profile:
    def_init_(self,id,name,age):
        print(id,name,age)

 # obj = profile(1,"sid",29)


 #? Eg:4
 class c1:sai@gamail.com
     name = "sid"
     place = "cbe"

     def m1(self)
     name = "sid"
     place = "cbe"
     print(name,place)
     print(self.email)
     



#? Eg:5
     class c1:
         def m1(self):
             name = "sid"
             age = 28

    def display(self):
        print(name,age)
        #! print(self.name,self.age)
        # ! print(self.name,self.age)
        print(self.m1())


#object = c1()
#object.display()
        #?Eg:6
        # To use the variable inside the constructor in another methods
        class class1:
            #email = "sid@gamil.com"        #static variable
            def_init_(self):
         self. name = "sid"     
          self. email = "sid@gmail.com"
        # return name,email # error -->cannot use return with construct
            
            def display(self):
                print(self.name,self.email)

   # c1 = class1()
  #c1.display()
    

#!------->Inheritance
#   the process of utilising the methods and attributes of parent class
#  throught the object of child it is called as inheritnce



# ? 5 types of Inheritance
# single Inheritance
#multilevel Inheritance
#multiple Inheritance
#Hybrid Inheritance
#Heirarical inheritance


#*single Inheritance
# ? it has only one parent class and only one chile class
# !Eg:1
    class parent:
        def m1 (self):
            print("Iam parent class")


parent.m1()

class child:
    def m2(self):
        print("Iam child class")


obj = dhid()
obj.m1()

# ! Eg:2
class c1:
    def_init_(self):
        print("Ia constructor from parent class")


 #class child1(c1):
 #  pass
 # odj = child1()

 # ! Eg:3
 class parent:
     name = "sidhu"


     class child(paraent):
         name = "name1"

         def disply(self):
             print(self.name)


  # d = child()
 # d.display()

# ! multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")


class voice:
    def dog_voice(self):
        print("bark")

class voice:
    def cat_voice(self):
        print("meow")

class voice:
    def parrot_voice(self):
        print("speak")
     
 all = parrot()
 all = dog._voice()
 # all.cat_voice()
 # all.sound()
 #all.parrot_voice()

# ? Eg:2
class honda_city:
    def honda_city_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)
        
    def honda_city__engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)

class amaze(honda_city):
    def amaze_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)


    def amaze_body_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

class civic(amaze):
    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)


class Honda(civic):
    pass

honda = Honda()
honda.honda_city_engin_specs(1500, 230, 2979, "petrol" 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")

# ! multiple inheritance
# ? it has multiple parent and 1 child

class while_pertol:
    def fuction_w(self):
        print("used for Bike,cars")

class premium_petrol:
    def function_p(self):
        print("spots cars,bikes")

        class petrol (while_pertol,organic_petrol,premium_petrol):
            def defanition(self):
                print("petrols types")


        
 # ? Eg:2
class honda_city:
    def honda_city_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)
        
    def honda_city__engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)

class amaze(honda_city):
    def amaze_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)


    def amaze_body_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

class civic(amaze):
    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)


class Honda(civic):
    pass

honda = Honda()
honda.honda_city_engin_specs(1500, 230, 2979, "petrol" 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")

# ! multiple inheritance
# ? it has multiple parent and 1 child
p = petrol()
p.defanition()
p.function_O()

# ! Eg:2
# MRO --> Method resolution order
class addition:
    def add(self, a, b):
        print(a+b)

    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subtract, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc,mul(4, 2)

# ! heirarical inheritance
class catagory:
    def cat_name(self):
        color="black"
        taste = "neutral taste")

    class carrot(catagoiry):
        def carrot_speecs(self):
            color="black"
            taste "neutral taste")

            self.display(colr,taste)
    class carrot(catagory):

        def carrot_specs(self):
            #color="green"
            #taste = "sweet"
            # self.display(color,taste)


    # = Tomato()
    #t.tomato_specs()
    #t.weight("20gms")

    # ! Hybrid inheritance
    #? The combionation of above 4 inheritance is called Hybrid inherit

    clas c3:
        def m3(self):
            print("class3")


        classc3:
            def m3 (self):
                print("class2")
                class c4:
                    def m4(self):
                        print("classs3")
                 class c5:
                     def m4(c2):
                         def m3(self)
                         print("class4")



            class c6(c5,c4,c2,c1):
                def m6(self):
                    print("class4")

        obj = c6()
        obj.m3()

# * ploymorphism in operators
# +
# print(8+8)
#print("k+1")
#print[1,2,3]+[5,6]}



#*
print(6*7)
11 = {12,3,4,5,6}
#print(*11)
#def f1(*args)
#def f1(*args)
# 11= [1,2,3,4]
#print(11*10)


#ploymorphism in classes
#we can achieve polymorphism in 2ways
#1.) method overloding -->it is not possible in python
#2.) method overriding


#1.)Tasks
d1 = {"shirt"1000,"pant":1500,"shoes:"900","handkey":30}
      #1.)Find the min ans max priced product
      #2.) Find the product starts with's' and 's'

      #2.)Find the n= 67,is strong number or not
      #3.)11 = {1,2,3,4,5,6]
      #n=2-->[5,6,1,2,3,4]
      #n=-->[4,5,6,1,2,3]

      

            
         
        
    













        
        



             

     













 














