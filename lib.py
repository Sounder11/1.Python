class functionass():
    
    def subfields():
        Lists=["sub-fields in AI are:","   ","Machine Learning","Neural Networks","vision","Robotics","speech Processing","Netural Langauage processing"]
        for AI in Lists:
            print(AI)
        
    def Oddeven():
        var=int(input("Enter the number:"))
        if(var%2==0):
            print(var," is even number")
        else:
            print(var," is odd number")
            
        
    def Elegible():
            A=("male")
            B=("female")
            data1=input("Your Gender:")
            if(data1==A):
                    age=int(input("Enter your age:"))
                    if(age>22):
                            print("Elegible")
                    else:
                            print("Not Elegible")
            elif(data1==B):
                    Age1=int(input("Enter your age:"))
                    if(Age1>18):
                            print("Elegible")
                    else:
                            print("Not Elegible")
            
    def percentage():
        Lists1=("subject1=23","subject2=45","subject3=34","subject4=23","subject5=23")
        for add in Lists1:
            print(add)
            subject1=23
            subject2=45
            subject3=34
            subject4=23
            subject5=23
            total=(subject1+subject2+subject3+subject4+subject5)
            print("Total=",total)
            percent=(total/500*100)
            print("percent=",percent)
    
        def triangle():
            data1=int(input("Height:"))
            data2=int(input("Breadth:"))
            Area_of_formula=(data1*data2)/2
            print("Area formula:(Height*Breadth)/2")
            print("Area of triangle:",Area_of_formula)
            data3=int(input("Height1:"))
            data4=int(input("Height2:"))
            data5=int(input("Breadth:"))
            print("perimeter formula:Height1+Height2+Breadth")
            perimeter=(data3+data4+data5)
            print("perimeter of triangle:",perimeter)