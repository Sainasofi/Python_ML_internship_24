# class A:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def fun1(self):
#         print("This is fun1 from class A")

# class B(A):
#     def __init__(self):
#         self.a=11e
#         self.b=22
#     #def fun1(self):
#          suoer().fun1()
#        #print("This is fun1 from class B")

# if __name__=="__main__":
#     obj = B()

#     print(obj.a)
#     print(obj.b)
#     obj.fun1()

# import numpy as np

# # Create a NumPy array
# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# import numpy as np

# # Sample scores data
# scores = np.array([[85, 90, 78],
#                    [92, 88, 95],
#                    [76, 95, 85],
#                    [90, 85, 92],
#                    [88, 76, 89]])

# # Calculate the mean score of each subject (across all students)
# subject_means = np.mean(scores, axis=0)
# print("Mean score of each subject:", subject_means)

# # Find the median score of each student (across all subjects)
# student_medians = np.median(scores, axis=1)
# print("Median score of each student:", student_medians)

# # Extract the scores of the student with the highest total score (sum of all subjects)
# highest_total_index = np.argmax(np.sum(scores, axis=1))
# highest_total_scores = scores[highest_total_index]
# print("Scores of the student with the highest total score:", highest_total_scores)

# # Find the minimum and maximum scores in each subject
# subject_mins = np.min(scores, axis=0)
# subject_maxs = np.max(scores, axis=0)
# print("Minimum score of each subject:", subject_mins)
# print("Maximum score of each subject:", subject_maxs)

# # Reshape the array to have shape (3, 5)
# scores_reshaped = np.transpose(scores)
# print("Reshaped array:", scores_reshaped)

# # Sort the scores of each subject in ascending order
# sorted_scores = np.sort(scores_reshaped, axis=1)
# print("Sorted scores:", sorted_scores)

#Exception Handling
# L= [1,2,3,4,5]
# print("Hello World")
# L
# L[3]
# try:
#     print (L[7])
# except:
#     print ("Index Error")
# print("end of code")
# a=10
# b=20

# try:
#     print(a/b)
# except:
#     print("B can't be zero")
# finally: 
#     print("Code executed succesfully")

#pandapractice
# import numpy as np
# import pandas as pd


# dic={
#     "Name": ["Tom", "nick", "krish", "jack"],
#     "Roll no": [1,2,3,4],
#     "Grades":["A", "B", "C", "C"],
#     "Email":["abc@xyz.com", "def@xyz.com", "ghi@xyz.com", "jkl@xyz.com"]
# }
# print(dic)
# df = pd.DataFrame(dic)
# print(df)
# print(df.head(2))
# print(df.tail(2))
# print(df.info())
# print(df.describe())
# print(df["Name"])
# print(df["Name"][0])
# print(df.loc[0,"Name"])
# print(df.loc[0,"Roll no"])
# print(df.loc[0,"Grades"])
# print(df.loc[0,"Email"])
# print(df.loc[0])
# print(df.loc[[0,2]])
# print(df.loc[0:2])
# print(df.loc[0:2,"Name"])
# print(df.loc[0:2,["Name","Roll no"]])
# print(df.loc[0:2,["Name","Roll no","Grades"]])
# print(df.loc[0:2,["Name","Roll no","Grades","Email"]])

# cus = pd.read_csv('Customer Table Level 1.csv')
# print(cus)
# print(type(cus))
# print(cus.index)
# print(cus.columns)
# print(cus.to_numpy)
# print(cus.drop(3))
# print(cus.loc[tuple((np.arange(48,78))), ('Company Name', 'Customer Name')])
# from matplotlib import pyplot as plt
# sm = pd.read_csv('student_marks.csv')
# # print(sm)
# sm['Total']=sm[['English', 'Hindi', 'Maths','Science', 'SST']].sum(axis=1)
# # print(sm)
# sm['Percentage']=sm['Total']/5
# print(sm)
# # A=100-80
# # B=80-60
# # C=60-50
# # D=50-40
# # E=40-30
# # F=0-30
# def assign_grade(percentage):
#     if percentage >= 80 :
#         return 'A'
#     elif percentage >= 60:
#         return 'B'
#     elif percentage >= 40:
#         return 'C'
#     elif percentage >= 30:
#         return 'D'
#     else:
#         return 'F'
# sm['Grade'] = sm['Percentage'].apply(assign_grade)
# # print(sm)
# # plt.figure(figsize=(10,6))

# temp=sm.head()
# temp
# sub=['English', 'Hindi', 'Maths','Science', 'SST']
# #col=['b','g','r','y','m']

# plt.figure(figsize=(10,5))
# #plt.plot(temp['Name'],temp[sub],marker='o',color=col[i],label=sub)
# plt.plot(temp['Name'],temp[sub],marker='o',label=sub)
# plt.title("Marks in different subjects")
# plt.xlabel('Name')
# plt.ylabel('Marks')
# plt.legend()
# plt.grid(True)
# plt.show()
