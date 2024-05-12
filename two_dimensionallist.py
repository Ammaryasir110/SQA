students_data=[["roll no", "Name", "Fathers NAme", "Caste", "Course", "Marks"],
[1,"Ammar","Yasir","Dahar","SQA","99"],
[2,"sami","aslam","shaikh","SQA","90"],
[3,"zain","ismail","soomro","SQA","85"]]
print(len(students_data))
print(students_data[2][5])
#method 2: using loop in above

#two dimensional list using loop:

students_data=[["roll no", "Name", "Fathers NAme", "Caste", "Course", "Marks"],
[1,"Ammar","Yasir","Dahar","SQA","99"],
[2,"sami","aslam","shaikh","SQA","90"],
[3,"zain","ismail","soomro","SQA","85"]]
print(len(students_data))
for i in students_data:
    print(i[2])
#matrices

a=[[3,4],[9,8]]
b=[[7,2],[0,1]]
r=[[0,0],[0,0]]

r[0][0]=(a[0][0]+b[0][0])
r[0][1]=(a[0][1]+b[0][1])
r[1][0]=(a[1][0]+b[1][0])
r[1][1]=(a[1][1]+b[1][1])