from easygui import *
upperbound = int(enterbox("Please, enter the number of course you have taken this semester: "))
file = open("courses.txt")
list=[]

coursesD = {}
for line in file:
    picked = line.strip().split(",")
    for i in picked:
        coursesD[picked[1]] = int(picked[2])

for course_names in coursesD:
    list.append(course_names)
msgbox(list[0:6])
msgbox(list[6:12])
msgbox(list[12:18])

def calculator():
    count = 0
    list_of_totals = []
    list_of_etcs = []
    while count <= upperbound:
        cname = enterbox("Then, please enter course full name: ")
        grade = int(enterbox("Finally, enter the relevant grade from this course: "))
        etcs = coursesD[cname]
        etc_x_grade = int((coursesD[cname] * grade))
        list_of_totals.append(etc_x_grade)
        list_of_etcs.append(etcs)
        count +=1
        if count == upperbound:
            break
    result = round(((sum(list_of_totals)/sum(list_of_etcs))*5)/100, 2)
    return "Your final GPA is "+str(result)+" for this semester!!!"

msgbox(calculator())


#open file(with making txt file) : 0.6 hour
#making coursesD dictionary(nested for loop(keys,values), strip,split functions) : 1.9 hours
# calculator def function : 2.1 hours
    # while (break) loop: 1.7 hours
        # making list_of_totals and list_of_etcs lists: 1.4 hour
        # inputs or enterboxs : 0.3 hour
    # result (with round funtion): 0.4 hour 
# easyGUI(messagebox, enterbox) :  0.5 hour
# total : 5.1 hours (all times are approximate)


    

    


    
        
    
        
        
        
    


