3#example

# class A:
#     def method(self):
#         print("while come to the python method1")
#
# class B(A):
#     def method1(self):
#         print("hello world frd")
#
# mc=B()
# mc.method1()

#example multilevel inheritance

class A:
    i,j=25,56
    def method(self):
        print(self.i+self.j)

class B(A):
    a,b=65,8
    def method1(self):
        print(self.a-self.b)

class C(B):
    x,d=8,2
    def method2(self):
        print(self.x*self.d)

mc=C()
mc.method2()

