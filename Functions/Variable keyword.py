# **kwargs variable number of keyword arguments to a function.
# Its a convention that allows to write keyword argument 0 or more. 
  #**kwargs is a dictionary

def student_details(sid, sname, **marks):    
    if len(marks) == 0:
        print(f"{sname} did not attend the exam")
    else:    
         percent = sum(marks.values()) / len(marks)                                     
         print(f"{sname} with id {sid} secures {percent}%")

student_details(101, "John", sub1=78.5, sub2=81.0, sub3=90.5)
student_details(102, "Carol", sub4=78.0, sub2=88.5, sub1=90.5, sub5=85.5)


print("----------------WITH *args AND **kwargs-------------------")

def student_details(sid, sname, *extra, **marks):        #** should be a last argument always.
    if len(marks) == 0:
        print(f"{sname} did not attend the exam")
    else:    
         percent = sum(marks.values()) / len(marks)                                     
         print(f"{sname} with id {sid} secures {percent}%")

    print(f"{sname} does {extra}")

student_details(101, "John", 'football', sub1=78.5, sub2=81.0, sub3=90.5)
student_details(102, "Carol", 'tennis', 'debate', sub4=78.0, sub2=88.5, sub1=90.5, sub5=85.5)