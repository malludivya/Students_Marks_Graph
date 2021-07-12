#importing library
import matplotlib.pyplot as plt

#creating the details of students

student_name=["Divya","Anil","Lokesh","Ramya","Lokesh"]
student_marks=[30,50,20,50,25]
marks_percentage=[30*100/50,50*100/50,20*100/50,50*100/50,25*100/50]

#defining a function for line graph

def Line_chart_of_student_and_marks():
    
    plt.plot(student_name,student_marks)
    plt.title("students marks graph")
    plt.xlabel("students names")
    plt.ylabel("students marks")
    plt.xlim(xmin = 0,xmax = 5)
    plt.ylim(ymin = 1,ymax = 50)
    plt.grid(True)
    plt.show()

#defining a function for bar graph
    
def Bar_chart_of_student_and_percentage():
    
    left_edges=student_name
    height=marks_percentage
    plt.bar(left_edges,height)
    plt.title("students percentage graph")
    plt.xlabel("student Names")
    plt.ylabel("student percentage")
    plt.show()
    
Line_chart_of_student_and_marks()

Bar_chart_of_student_and_percentage()
