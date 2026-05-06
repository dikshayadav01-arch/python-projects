#single level inheritance
class A:
    def state1(self):
        print("state present")
    def state2(self):
        print("state2 present")        
class B(A):
    def state3(self):
        print("state3 present")            
    def state4(self):
        print("state4 present")
#multi-level inheritance        
class C(B):
    def state5(self):
        print("state5 present")
    def state6(self):
        print("state6 present") 
c=C()
c.state1()
c.state3()
c.state5()
