special_triangles = [(3,4,5),(5,12,13),(8,15,17),(7,24,25)]

class Pythagorean_Detector():

    def __init__(self, n):
        self.n = n
    
    def func(self):
        flag = False
        for i in special_triangles:
            k = int(1)
            total = 0
            while total < self.n:
                total = i[0]*k + i[1]*k + i[2]*k
                k += 1
            if total == self.n:
                flag = True
                break
        self.print_(i, k-1, total, flag)
          

    def print_(self,i,k,total,flag):
        if flag == True:
            print(i[0]*k," + ",i[1]*k," = ",i[2]*k)
            print(i[0]*k," + ",i[1]*k," + ",i[2]*k," = ",total)
            print(total," is compatible with Pythagorean triple!")

        else:
            print("The entry value is not compatible with Pythagorean triple set!")

obj = Pythagorean_Detector(int(input("Enter the N value:")))
obj.func()


    
