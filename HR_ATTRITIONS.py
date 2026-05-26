# MAKING THE HR ATTRITION PROJECT THEN ANALUSICS AND THE VISUALTIZATION ALL THE DATA AND FIND THE INSIGHTS AND PREDICTION THE DATA 
# import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
conn= mysql.connector.connect(
    host="localhost",
    user ="root",
    password="Gurvinder@SQL2026",
    database="HR_PROJECT"
)
query="select * from HR_ATTRITION"
# print the sql data
df =pd.read_sql(query,conn)
print(df)

# then understand the data
print(df.head())
print(df.info())
print(df.describe())

# extra extensions
# making the first subplot of the kpi dashboars 
fig,ax =plt.subplots(3,2,figsize =(15,10))
fig.suptitle("Kpi Dashboard",fontweight="bold")
# then making the Kpi Dashboard 
Total_Employees =df["EmployeeCount"].sum()
print("Total Employee",Total_Employees)
# Total Employees KPI
Total_Employees = len(df)
ax[0,0].text(
    0.5,
    0.5,
    f"Total Employees\n{Total_Employees}",
    ha="center",
    va="center",
    fontsize=22,
    fontweight="bold",
    color="blue"
)
ax[0,0].set_facecolor("whitesmoke")
ax[0,0].set_title("Total Employess",fontweight="bold")
ax[0,0].grid()

# remove axis
# ax[0,0].axis("off")
# attrition rate 
Attrition_Rate =df["Attrition"].value_counts() 
print("Attrition Rate",Attrition_Rate)
colors=["pink","grey"]

ax[0,1].pie(Attrition_Rate.values,labels =Attrition_Rate.index,autopct='%1.1f%%',colors=colors,shadow=True)
ax[0,1].set_title("Attrition Rate Distributions",fontweight ="bold")
ax[0,1].set_ylabel("Count",fontweight="bold")
ax[0,1].set_xlabel("Attrition Rate",fontweight="bold")
ax[0,1].grid()

# then the average salary
Average_Salary =df["MonthlyIncome"].mean().round(2)
print("Average Salary",Average_Salary)
# making the kpi charts
ax[1,0].text(0.5,0.5,f"Average Salary :{Average_Salary}",ha="center",va="bottom",fontsize=20,color="green",fontweight="bold")
ax[1,0].set_facecolor("whitesmoke")
ax[1,0].set_title("Average Salary",fontweight="bold")
ax[1,0].grid()


# average Age
Average_age = df["ï»¿Age"].mean().round(2)
print("Averge Age",Average_age)
# making the kpi charts
ax[1,1].text(0.5,0.5,f"Average Age :{Average_age}",ha="center",va="bottom",fontsize=20,color="brown",fontweight="bold")
ax[1,1].set_facecolor("whitesmoke")
ax[1,1].set_title("Average Age",fontweight="bold")
ax[1,1].grid()

# overtime emoloyess
Overtime_Employees =(len(df[df["OverTime"]=="Yes"])/len(df)) *100
print("Average Overtime",Overtime_Employees)
ax[2,0].text(0.5,0.5,f"Average OverTime :{Overtime_Employees}",ha="center",va="bottom",fontsize=20,color="grey",fontweight="bold")
ax[2,0].grid()
ax[2,0].set_title("Average Overtime",fontweight="bold")

# gender count
Gender_Employess = df["Gender"].value_counts(normalize=True) * 100

print("Gender_Employess", Gender_Employess)

Male_Percentage = Gender_Employess.get("Male", 0)
Female_Percentage = Gender_Employess.get("Female", 0)
# KPI CARD
ax[2,1].text(
    0.5,
    0.75,
    "👨",
    ha="center",
    fontsize=30
)

ax[2,1].text(
    0.5,
    0.5,
    f"{Male_Percentage:.1f}%",
    ha="center",
    va="center",
    fontsize=26,
    color="blue",
    fontweight="bold"
)

ax[2,1].text(
    0.5,
    0.25,
    "Male Employees",
    ha="center",
    fontsize=10,
    color="gray"
)

ax[2,1].set_title(
    "Gender KPI Dashboard",
    fontweight="bold"
)

ax[2,1].set_facecolor("#f5f5f5")

# Border
for spine in ax[2,1].spines.values():
    spine.set_visible(True)
    spine.set_edgecolor("black")
    spine.set_linewidth(2)
ax[2,1].set_xlabel("Maximum Percentage of Attritions",fontweight="bold")
# Remove Axis
ax[2,1].set_xticks([])
ax[2,1].set_yticks([])

plt.tight_layout()
# plt.show()




# then making the first subplot of the Hr attrition analysics  Deshboard
Yes_Attrition =df[df["Attrition"]=="Yes"]

# Subplot 1 Hr Attrition Analysics Dashboard
fig,ax = plt.subplots(4,3,figsize=(20,10))

fig.suptitle("HR DistriBution Analysics Deshboard",fontweight="bold",color="Brown")
# making the subplot of the Attrition Distributions 
containers=sns.countplot(x="Attrition",data=df,palette="viridis",ax=ax[0,0])
# br =ax[0,0].bar(Attrition_Dist["Attrition"],Attrition_Dist["count"],edgecolor="black",color="grey",label="Attrition Distribution")
ax[0,0].set_title("Attrition Distribution",fontweight ="bold")
# ax[0,0].bar_label(br,padding=5,color="blue",fontweight="bold")
for container in ax[0,0].containers:
    ax[0,0].bar_label(container,fontsize=8,color="green")
ax[0,0].legend(title="Attrition Analysics")
ax[0,0].grid(True)
ax[0,0].set_xlabel("Attritions",fontweight="bold")
ax[0,0].set_ylabel("Count",fontweight="bold")
ax[0,0].tick_params(axis ="x")
ax[0,0].tick_params(axis ="y")

# making the plot of the Age vs attritions
Age_Attrition =Yes_Attrition["ï»¿Age"].value_counts().sort_index()
ag=ax[0,1].bar(Age_Attrition.index,Age_Attrition.values,color="pink",edgecolor="black",label="Attrition Distributions")
ax[0,1].set_title("Age Attrition Distribution",fontweight ="bold")
# ax[0,1].bar_label(ag,padding=5,color="blue",fontweight="bold")
ax[0,1].legend(title= "Age VS Attrition Distribution")
ax[0,1].grid(True)
ax[0,1].set_xlabel("Attritions",fontweight="bold")
ax[0,1].set_ylabel("Age",fontweight="bold")
ax[0,1].tick_params(axis ="x",rotation=90,labelsize=6)
ax[0,1].tick_params(axis ="y")

# Making the plot in Which Analysics the Maximum Attriton Which AGE and Minimum Which Age
Yes_Attrition =df[df["Attrition"]=="Yes"]

Age_Attrition =Yes_Attrition["ï»¿Age"].value_counts().sort_index()
Max_Age_Values = Age_Attrition.idxmax()
Max_Age_Count =Age_Attrition.max()
# Minimum Age Distribution by Attritions
Min_Age_Values = Age_Attrition.idxmin()
Min_Age_Count =Age_Attrition.min()
# then check the color of the maximum attrition age and the minimum attriiton age and show in the same plot
Age_Color =[]
for value in Age_Attrition.index:
    if value ==Max_Age_Values:
        Age_Color.append("green")
    elif value == Min_Age_Values:
        Age_Color.append("red")
    else:
        Age_Color.append("whitesmoke")

ax[0,2].bar(Age_Attrition.index,Age_Attrition.values,edgecolor="black",label="Age Maximum & Minimum Attriton",color=Age_Color)
ax[0,2].set_title("Age Maximum & Minimum Attrition Distribution",fontweight="bold")
ax[0,2].text(Max_Age_Values,Max_Age_Count,f"Max_Age {Max_Age_Count} Having Maximum Attrition",ha="center",va="bottom",color="green",fontweight="bold")
ax[0,2].text(Min_Age_Values,Min_Age_Count,f"Max_Age {Min_Age_Values} Having Minimum Attrition",ha="center",va="bottom",color="red",fontweight="bold")
ax[0,2].grid(True)
ax[0,2].set_xlabel("Attritions",fontweight="bold")
ax[0,2].set_ylabel("Age",fontweight="bold")
ax[0,2].tick_params(axis ="x",rotation=90,labelsize=6)
ax[0,2].legend()
ax[0,2].tick_params(axis ="y")

# Gender Attrition Analysics Distributes
Gender_Attrition =Yes_Attrition["Gender"].value_counts().sort_index()
print(Gender_Attrition)
gn=ax[1,0].bar(Gender_Attrition.index,Gender_Attrition.values,color="grey",edgecolor="black",label="Gender Attrition",width=0.3)
ax[1,0].bar_label(gn,padding=5,fontweight="bold",color="blue")
ax[1,0].set_title("Gender Attrition Distribution",fontweight="bold")
ax[1,0].grid(True)
ax[1,0].set_xlabel("Attritions",fontweight="bold")
ax[1,0].set_ylabel("Gender",fontweight="bold")
ax[1,0].legend()
# check the MAX Attrition by Gender
Max_Gender_values =Gender_Attrition.idxmax()
Max_Gender_count =Gender_Attrition.max()
Gender_color =[]
for Gender_bar in Gender_Attrition:
    if Gender_bar == Max_Gender_count:
        Gender_color.append("green")
    else:
        Gender_color.append("whitesmoke")

ax[1,1].bar(Gender_Attrition.index,Gender_Attrition.values,color= Gender_color,edgecolor="black",label="Maximum Gender Attrition",width=0.3)
ax[1,1].text(Max_Gender_values,Max_Gender_count,f"Max Gender Category {Max_Gender_values} Having Maximum Attrition",ha="center",va="bottom",color="green",fontweight="bold")
ax[1,1].set_title("Maximum Gender Attrition Distribution",fontweight="bold")
ax[1,1].grid(True)
ax[1,1].set_xlabel("Gender",fontweight="bold")
ax[1,1].set_ylabel("Attrition",fontweight="bold")
ax[1,1].legend()
# minimum Age Attrition
Min_Gender_values =Gender_Attrition.idxmin()
Min_Gender_count =Gender_Attrition.min()
Gender_color =[]
for Gender_bar in Gender_Attrition:
    if Gender_bar == Min_Gender_count:
        Gender_color.append("red")
    else:
        Gender_color.append("whitesmoke")

ax[1,2].bar(Gender_Attrition.index,Gender_Attrition.values,color= Gender_color,edgecolor="black",label="Minimum Gender Attrition",width=0.3)
ax[1,2].text(Min_Gender_values,Min_Gender_count,f"Min Gender Category {Min_Gender_values} Having Minimum Attrition",ha="center",va="bottom",color="red",fontweight="bold")
ax[1,2].set_title("Minimum Gender Attrition Distribution",fontweight="bold")
ax[1,2].grid(True)
ax[1,2].set_xlabel("Gender",fontweight="bold")
ax[1,2].set_ylabel("Attrition",fontweight="bold")
ax[1,2].legend()
# making the plot of the Department Wish Attriton 
Department_Attrition =Yes_Attrition["Department"].value_counts().sort_index()
gn=ax[2,0].bar(Department_Attrition.index,Department_Attrition.values,color="purple",edgecolor="black",label="Department Attrition",width=0.3)
ax[2,0].bar_label(gn,padding=5,fontweight="bold",color="blue")
ax[2,0].set_title("Department Attrition Distribution",fontweight="bold")
ax[2,0].grid(True)
ax[2,0].set_xlabel("Attritions",fontweight="bold")
ax[2,0].set_ylabel("Department",fontweight="bold")
ax[2,0].tick_params(axis="x",labelsize=6)
ax[2,0].legend()
# Making the Maximum Depertment Attrition
Max_Department_values =Department_Attrition.idxmax()
Max_Department_count =Department_Attrition.max()
Depart_color =[]
for Department_bar in Department_Attrition:
    if Department_bar == Max_Department_values:
        Depart_color.append("green")
    else:
        Depart_color.append("whitesmoke")

ax[2,1].bar(Department_Attrition.index,Department_Attrition.values,color= Depart_color,edgecolor="black",label="Maximum Department Attrition",width=0.3)
ax[2,1].text(Max_Department_values,Max_Department_count,f"Max Department having {Max_Department_values} Having Maximum Attrition",ha="center",va="bottom",color="green",fontweight="bold")
ax[2,1].set_title("Maximum Department Attrition Distribution",fontweight="bold")
ax[2,1].grid(True)
ax[2,1].set_xlabel("Deparment",fontweight="bold")
ax[2,1].set_ylabel("Attrition",fontweight="bold")
ax[2,1].tick_params(axis="x",labelsize=6)
ax[2,1].legend()
# min Department having Minimum Attrition
Min_Department_values =Department_Attrition.idxmin()
Min_Department_count =Department_Attrition.min()
Depart_color =[]
for Department_bar in Department_Attrition:
    if Department_bar == Min_Department_count:
        Depart_color.append("red")
    else:
        Depart_color.append("whitesmoke")

ax[2,2].bar(Department_Attrition.index,Department_Attrition.values,color= Depart_color,edgecolor="black",label="Minimum Department Attrition",width=0.3)
ax[2,2].text(Min_Department_values,Min_Department_count,f"Min Department having {Min_Department_values} Having Minimum Attrition",ha="center",va="bottom",color="red",fontweight="bold")
ax[2,2].set_title("Minimum Department Attrition Distribution",fontweight="bold")
ax[2,2].grid(True)
ax[2,2].set_xlabel("Deparment",fontweight="bold")
ax[2,2].set_ylabel("Attrition",fontweight="bold")
ax[2,2].tick_params(axis="x",labelsize=6)
ax[2,2].legend()
# education field vs attritions 
EducationField_Attrition =Yes_Attrition["EducationField"].value_counts().sort_index()
print(EducationField_Attrition)
ed=ax[3,0].bar(EducationField_Attrition.index,EducationField_Attrition.values,color="skyblue",edgecolor="black",label="Education_Field Vs Attrition",width=0.3)
ax[3,0].set_title("Eduction_field Attrition Distributions",fontweight="bold")
ax[3,0].bar_label(ed,padding=5,fontweight="bold",color="blue")
ax[3,0].set_title("Eductions_Field Attrition Distribution",fontweight="bold")
ax[3,0].grid(True)
ax[3,0].set_xlabel("Attritions",fontweight="bold")
ax[3,0].set_ylabel("Eduction_Field",fontweight="bold")
ax[3,0].tick_params(axis="x",labelsize=6)
ax[3,0].legend()
# maximum Education type
EducationField_Attrition =Yes_Attrition["EducationField"].value_counts().sort_index()
print(EducationField_Attrition)
Max_Eduction_Values =EducationField_Attrition.idxmax()
Max_Eduction_Count=EducationField_Attrition.max()
educt_color=[]
for Educt in EducationField_Attrition.index:
    if Educt ==Max_Eduction_Values:
        educt_color.append("green")
    else:
        educt_color.append("whitesmoke")
ed=ax[3,1].bar(EducationField_Attrition.index,EducationField_Attrition.values,color=educt_color,edgecolor="black",label="Maximum Education_Field Vs Attrition",width=0.3)
ax[3,1].set_title("Maximum Eduction_field Attrition Distributions",fontweight="bold")
ax[3,1].text(Max_Eduction_Values,Max_Eduction_Count,f"Maximum Eduction_Field {Max_Eduction_Values}",color="green",fontweight="bold")
ax[3,1].bar_label(ed,padding=5,fontweight="bold",color="blue")
ax[3,1].grid(True)
ax[3,1].set_xlabel("Attritions",fontweight="bold")
ax[3,1].set_ylabel("Eduction_Field",fontweight="bold")
ax[3,1].tick_params(axis="x",labelsize=6)
ax[3,1].legend()
# minimum education_type attritions 
Min_Eduction_Values =EducationField_Attrition.idxmin()
Min_Eduction_Count=EducationField_Attrition.min()
educt_color=[]
for Educt in EducationField_Attrition.index:
    if Educt ==Min_Eduction_Values:
        educt_color.append("red")
    else:
        educt_color.append("whitesmoke")
ed=ax[3,2].bar(EducationField_Attrition.index,EducationField_Attrition.values,color=educt_color,edgecolor="black",label="Minimum Education_Field Vs Attrition",width=0.3)
ax[3,2].set_title("Minimum Eduction_field Attrition Distributions",fontweight="bold")
ax[3,2].text(Max_Eduction_Values,Max_Eduction_Count,f"Maximum Eduction_Field {Max_Eduction_Values}",color="red",fontweight="bold")
ax[3,2].bar_label(ed,padding=5,fontweight="bold",color="blue")
ax[3,2].grid(True)
ax[3,2].set_xlabel("Attritions",fontweight="bold")
ax[3,2].set_ylabel("Eduction_Field",fontweight="bold")
ax[3,2].tick_params(axis="x",labelsize=6)
ax[3,2].legend()

plt.tight_layout()
# plt.show()

# Subplot 2 Salary vs Attrtions  
fig,ax =plt.subplots(3,3,figsize=(15,10))
fig.suptitle("Salary Attrition Deshboard",fontweight="bold")
# Making the Subplot of the monthly Income and attrition then find the maximum and minimum salary Attritions
Salary_Attrition =Yes_Attrition["MonthlyIncome"].value_counts().sort_index()
counts, bins, patches=ax[0,0].hist(data=Yes_Attrition,x="MonthlyIncome",color="brown",label ="Salary Attrition Distributions")
max_val = Yes_Attrition["MonthlyIncome"].max()
min_val = Yes_Attrition["MonthlyIncome"].min()
max_i =counts.argmax()
ax[0,0].text((bins[max_i] + bins[max_i+1]) / 2,counts[max_i],
f"Min_Attrition_Salary",ha="center",va="bottom",color="red",fontweight="bold")
min_i =counts.argmin()
ax[0,0].text((bins[min_i] + bins[min_i+1]) / 2,counts[min_i] +2,
    f"Max_Attrition_Salary",ha="center", va="bottom",color="green",fontweight="bold")
ax[0,0].set_title("Salary Attrition Distribution", fontweight="bold")
ax[0,0].set_xlabel("Monthly Income")
ax[0,0].set_ylabel("Attrition Count")
ax[0,0].legend()
ax[0,0].grid()
# making the plot of work at the company
Campany_year=Yes_Attrition["YearsAtCompany"].value_counts().sort_index()
print("Campany Work",Campany_year)
# maximum year having maximum person work
# sns.countplot(x="YearsAtCompany",hue="Attrition",data=df,ax=ax[0,1])
cm=ax[0,1].bar(Campany_year.index,Campany_year.values,color="whitesmoke",edgecolor="black",label="Years at Company vs Attrition")
ax[0,1].bar_label(cm,padding =5,color ="blue",fontsize=6,fontweight ="bold")
ax[0,1].set_title("Years at Company vs Attrition", fontweight="bold")
ax[0,1].set_xlabel("Yearly Work ")
ax[0,1].set_ylabel("Attrition Count")
ax[0,1].legend()
ax[0,1].grid()
ax[0,1].tick_params(axis="x",labelsize=6,rotation =90)
# show the maximum  and minimum attrition in which year
Max_year_values =Campany_year.idxmax()
Min_year_Values =Campany_year.idxmin()
# count
Max_year_Count =Campany_year.max()
Min_year_Count =Campany_year.min()
Min_year =Campany_year[Campany_year==Min_year_Values].index

Campany_color =[]
for i in Campany_year.index:
    if Campany_year[i] ==Campany_year.max():
        Campany_color.append("green")
    elif Campany_year[i] ==Min_year.min():
        Campany_color.append("red")
    else:
        Campany_color.append("grey")
ax[0,2].bar(Campany_year.index,Campany_year.values,color=Campany_color,label=" Max & Min Years at Company vs Attrition")
ax[0,2].text(Max_year_values,Max_year_Count+1,f"Max Year Count of Attrition :{Max_year_Count}",fontweight ="bold",color="green")
ax[0,2].text(Min_year_Values,Min_year_Count+1,f"Min Year's Count of Attrition :{Min_year_Count}",fontweight ="bold",color="red")
ax[0,2].set_title("max and min Years at Company vs Attrition", fontweight="bold")
ax[0,2].set_xlabel("Yearly Work ",fontweight="bold")
ax[0,2].set_ylabel("Attrition Count",fontweight="bold")
ax[0,2].legend()
ax[0,2].grid()
ax[0,2].tick_params(axis="x",labelsize=6,rotation =90)

# then distance form home attritions
DistancefromHome =Yes_Attrition["DistanceFromHome"].value_counts().sort_index()
print("Distance From Home",DistancefromHome)
ds =ax[1,0].bar(DistancefromHome.index,DistancefromHome.values,edgecolor="black",color="orange",label="Distance From Home Vs Attrition")
ax[1,0].bar_label(ds,padding=5,fontsize=6,color="blue",fontweight="bold")
ax[1,0].set_title("Distance From Home Attritions",fontweight ="bold")
ax[1,0].set_xlabel("Distance From Home",fontweight="bold")
ax[1,0].set_ylabel("Attrition Count",fontweight="bold")
ax[1,0].legend()
ax[1,0].grid()
ax[1,0].tick_params(axis="x",labelsize=6,rotation =90)
# Check the Maximum Count of the Attriton by Distance From home
Max_Distancefromhome_value =DistancefromHome.idxmax()
Min_Distancefromhome_value =DistancefromHome.idxmin()
# count
Max_Distancefromhome_Count =DistancefromHome.max()
Min_Distancefromhome_Count =DistancefromHome.min()
distance_color =[]
for i in DistancefromHome.index:
    if DistancefromHome[i] == DistancefromHome.max():
        distance_color.append("red")
    else:
        distance_color.append("whitesmoke")
ax[1,1].bar(DistancefromHome.index,DistancefromHome.values,edgecolor="black",color=distance_color,label=" Max Distance From Home high Attrition")
ax[1,1].text(Max_Distancefromhome_value,Max_Distancefromhome_Count,f" Max Attrition if Maximum Distance From home :{Max_Distancefromhome_Count}",color="red",fontweight ="bold",fontsize=8)
ax[1,1].set_title("Distance From Home Attritions",fontweight ="bold")
ax[1,1].set_xlabel("Distance From Home",fontweight="bold")
ax[1,1].set_ylabel("Attrition Count",fontweight="bold")
ax[1,1].legend(loc="lower left")
ax[1,1].grid()
ax[1,1].tick_params(axis="x",labelsize=6,rotation =90)
# Minimum Attriton Check the Distance from Home
distance_color =[]
for i in DistancefromHome.index:
    if DistancefromHome[i] == DistancefromHome.min():
        distance_color.append("green")
    else:
        distance_color.append("whitesmoke")
ax[1,2].bar(DistancefromHome.index,DistancefromHome.values,edgecolor="black",color=distance_color,label=" Min Distance From Home Less Attrition")
ax[1,2].text(Min_Distancefromhome_value,Min_Distancefromhome_Count,f" Min Attrition if Minimum Distance From home :{Min_Distancefromhome_Count}",color="green",fontweight ="bold",fontsize=8)
ax[1,2].set_title("Distance From Home Attritions",fontweight ="bold")
ax[1,2].set_xlabel("Distance From Home",fontweight="bold")
ax[1,2].set_ylabel("Attrition Count",fontweight="bold")
ax[1,2].legend(loc="upper left")
ax[1,2].grid()
ax[1,2].tick_params(axis="x",labelsize=6,rotation =90)
# total_working_year vs attritons
Totalworkingyear =Yes_Attrition["TotalWorkingYears"].value_counts().sort_index()
print("Total Experience",Totalworkingyear)
ax[2,0].bar(Totalworkingyear.index,Totalworkingyear.values,edgecolor ="black",color="brown",label="Total Working Year")
ax[2,0].set_title("Total Working Year Attritions",fontweight ="bold")
ax[2,0].set_xlabel("Working_Wear",fontweight="bold")
ax[2,0].set_ylabel("Attrition Count",fontweight="bold")
ax[2,0].legend(loc="upper left")
ax[2,0].grid()
ax[2,0].tick_params(axis="x",labelsize=6,rotation =90)
# then visualization the maximum working year
Max_Totalyear_values =Totalworkingyear.idxmax()
Max_Totalyear_Count =Totalworkingyear.max()
distance_color =[]
for i in Totalworkingyear.index:
    if Totalworkingyear[i] == Totalworkingyear.max():
        distance_color.append("green")
    else:
        distance_color.append("whitesmoke")
ax[2,1].bar(Totalworkingyear.index,Totalworkingyear.values,edgecolor="black",color=distance_color,label=" Total Working Year Max year Attrition")
ax[2,1].text(Max_Totalyear_values,Max_Totalyear_Count,f" Min Attrition if Minimum Distance From home :{Max_Totalyear_Count}",color="green",fontweight ="bold",fontsize=8)
ax[2,1].set_title("Distance From Home Attritions",fontweight ="bold")
ax[2,1].set_xlabel("Total Working Year",fontweight="bold")
ax[2,1].set_ylabel("Attrition Count",fontweight="bold")
ax[2,1].legend(loc="lower left")
ax[2,1].grid()
ax[2,1].tick_params(axis="x",labelsize=6,rotation =90)
# check the minimum yearworking havinf minimum attritions
Min_Totalyear_values =Totalworkingyear.idxmin()
Min_Totalyear_Count =Totalworkingyear.min()
distance_color =[]
for i in Totalworkingyear.index:
    if Totalworkingyear[i] == Totalworkingyear.min():
        distance_color.append("red")
    else:
        distance_color.append("whitesmoke")
ax[2,2].bar(Totalworkingyear.index,Totalworkingyear.values,edgecolor="black",color=distance_color,label=" Total Working Year Min year Attrition")
ax[2,2].text(Max_Totalyear_values,Max_Totalyear_Count,f" Min Attrition if the Totalworking year is :{Max_Totalyear_Count}",color="red",fontweight ="bold",fontsize=8)
ax[2,2].set_title("Distance From Home Attritions",fontweight ="bold")
ax[2,2].set_xlabel("Total Working Year",fontweight="bold")
ax[2,2].set_ylabel("Attrition Count",fontweight="bold")
ax[2,2].legend(loc="lower left")
ax[2,2].grid()
ax[2,2].tick_params(axis="x",labelsize=6,rotation =90)

plt.tight_layout()
# plt.show()

#subplot 3 working  Environment Analysics
fig,ax =plt.subplots(3,3,figsize =(15,10))
fig.suptitle("Work Environment Anaylsis")
Job_Satisfictions_attrition=Yes_Attrition["JobSatisfaction"].value_counts().reset_index()
print("Job Satisifiction  Vs Attrition",Job_Satisfictions_attrition) 
br=ax[0,0].bar(Job_Satisfictions_attrition["JobSatisfaction"],Job_Satisfictions_attrition["count"],edgecolor="black",color="orange",label=" Job Satisfiction vs Attrition",width=0.3)
ax[0,0].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[0,0].set_title("Job Satisifictions Attritions",fontweight ="bold")
ax[0,0].set_xlabel("Job Satisfictions",fontweight="bold")
ax[0,0].set_ylabel("Attrition Count",fontweight="bold")
ax[0,0].legend(loc="lower left")
ax[0,0].grid()
ax[0,0].tick_params(axis="x",labelsize=6,rotation =90)

# making the maximum attriition having which Satisfication level
Job_Satisfictions_attrition=Yes_Attrition["JobSatisfaction"].value_counts().reset_index()
print("Job Satisifiction  Vs Attrition",Job_Satisfictions_attrition) 
Max_Job_Satisfiction_Values =Job_Satisfictions_attrition["JobSatisfaction"].idxmax()
Max_Job_Satisfiction_count =Job_Satisfictions_attrition["count"].max()
mx_col =[]
for satis in Job_Satisfictions_attrition["count"]:
    if satis ==Job_Satisfictions_attrition["count"].max():
        mx_col.append("red")
    else:
        mx_col.append("whitesmoke")

br=ax[0,1].bar(Job_Satisfictions_attrition["JobSatisfaction"],Job_Satisfictions_attrition["count"],edgecolor="black",color=mx_col,label="Max Level of  Job Satisfiction vs Attrition",width=0.3)
# ax[0,1].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[0,1].text(Max_Job_Satisfiction_Values,Max_Job_Satisfiction_count,f"Maximum unSatisfictions Level of the Attritions :{Max_Job_Satisfiction_count}",color="red",fontweight ="bold",fontsize=8)
ax[0,1].set_title("Maximum Level of Job unSatisifictions Attritions",fontweight ="bold")
ax[0,1].set_xlabel("Job Satisfictions",fontweight="bold")
ax[0,1].set_ylabel("Attrition Count",fontweight="bold")
ax[0,1].legend(loc="lower left")
ax[0,1].grid()
ax[0,1].tick_params(axis="x",labelsize=6,rotation =90)
# //minimum attritions
Job_Satisfictions_attrition=Yes_Attrition["JobSatisfaction"].value_counts().reset_index()
print("Job Satisifiction  Vs Attrition",Job_Satisfictions_attrition) 
Min_Job_Satisfiction_Values =Job_Satisfictions_attrition["JobSatisfaction"].idxmin()
Min_Job_Satisfiction_count =Job_Satisfictions_attrition["count"].min()
mn_col =[]
for satis in Job_Satisfictions_attrition["count"]:
    if satis ==Job_Satisfictions_attrition["count"].min():
        mn_col.append("green")
    else:
        mn_col.append("whitesmoke")

br=ax[0,2].bar(Job_Satisfictions_attrition["JobSatisfaction"],Job_Satisfictions_attrition["count"],edgecolor="black",color=mn_col,label="Min Level of  Job Satisfiction vs Attrition",width=0.3)
# ax[0,1].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[0,2].text(Min_Job_Satisfiction_Values,Min_Job_Satisfiction_count,f"Satisfictions Level of the Attritions :{Min_Job_Satisfiction_count}",color="green",fontweight ="bold",fontsize=8)
ax[0,2].set_title("Minimum Level of Job unSatisifictions Attritions",fontweight ="bold")
ax[0,2].set_xlabel("Job Satisfictions",fontweight="bold")
ax[0,2].set_ylabel("Attrition Count",fontweight="bold")
ax[0,2].legend(loc="lower left")
ax[0,2].grid()
ax[0,2].tick_params(axis="x",labelsize=6,rotation =90)
plt.tight_layout()
# plt.show()
# worklife balance 
Worklife_Balance =Yes_Attrition["WorkLifeBalance"].value_counts().reset_index()
print("Worklife Balance",Worklife_Balance)
br=ax[1,0].bar(Worklife_Balance["WorkLifeBalance"],Worklife_Balance["count"],edgecolor="black",color="orange",label="Worklife Balance vs Attrition",width=0.3)
ax[1,0].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[1,0].set_title("Worklife Balanec Attritions",fontweight ="bold")
ax[1,0].set_xlabel("Worklife Attrition",fontweight="bold")
ax[1,0].set_ylabel("Attrition Count",fontweight="bold")
ax[1,0].legend(loc="lower left")
ax[1,0].grid()
ax[1,0].tick_params(axis="x",labelsize=6,rotation =90)
# then making the maximum Worklife attriton of the whixh level
Max_Worklife_Balance_values =Worklife_Balance["WorkLifeBalance"].idxmax()
Max_Worklife_Balance_count =Worklife_Balance["count"].max()
mx_work =[]
for satis in Worklife_Balance["count"]:
    if satis ==Worklife_Balance["count"].max():
        mx_work.append("red")
    else:
        mx_work.append("whitesmoke")

br=ax[1,1].bar(Worklife_Balance["WorkLifeBalance"],Worklife_Balance["count"],edgecolor="black",color=mx_work,label= "Maximum WorkLife Balance Attrition",width=0.3)
# ax[0,1].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[1,1].text(Max_Worklife_Balance_values,Max_Worklife_Balance_count,f"Maximum WorkLife Balance Attrition:{Max_Worklife_Balance_count}",color="red",fontweight ="bold",fontsize=8)
ax[1,1].set_title("Maximum WorkLife Balance Attrition",fontweight ="bold")
ax[1,1].set_xlabel("Worklife Balance",fontweight="bold")
ax[1,1].set_ylabel("Attrition Count",fontweight="bold")
ax[1,1].legend(loc="lower left")
ax[1,1].grid()
ax[1,1].tick_params(axis="x",labelsize=6,rotation =90)
# minimum worklife balance minimum attrition level
Min_Worklife_Balance_values =Worklife_Balance["WorkLifeBalance"].idxmin()
Min_Worklife_Balance_count =Worklife_Balance["count"].min()
mn_work =[]
for satis in Worklife_Balance["count"]:
    if satis ==Min_Worklife_Balance_count:
        mn_work.append("green")
    else:
        mn_work.append("whitesmoke")

br=ax[1,2].bar(Worklife_Balance["WorkLifeBalance"],Worklife_Balance["count"],edgecolor="black",color=mn_work,label=" Minimum WorkLife Balance Attrition",width=0.3)
# ax[0,1].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[1,2].text(Min_Worklife_Balance_values,Min_Worklife_Balance_count,f"Minimum WorkLife Balance Attrition:{Max_Worklife_Balance_count}",color="green",fontweight ="bold",fontsize=8)
ax[1,2].set_title("Minimum Worklife Balance Attritions",fontweight ="bold")
ax[1,2].set_xlabel("Worklife Balance",fontweight="bold")
ax[1,2].set_ylabel("Attrition Count",fontweight="bold")
ax[1,2].legend(loc="lower left")
ax[1,2].grid()
ax[1,2].tick_params(axis="x",labelsize=6,rotation =90)
# environment Satisfications
EnvironmentSatisfaction_attrition =Yes_Attrition["EnvironmentSatisfaction"].value_counts().reset_index()
print("Environment Satisfactions Attritions",EnvironmentSatisfaction_attrition)
br=ax[2,0].bar(Worklife_Balance["WorkLifeBalance"],Worklife_Balance["count"],edgecolor="black",color="pink",label="Environment Satisfaction Balance vs Attrition",width=0.3)
ax[2,0].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[2,0].set_title("Environment_Satisfaction  Balance Attritions",fontweight ="bold")
ax[2,0].set_xlabel("Environment_Satisfaction Balance Attrition",fontweight="bold")
ax[2,0].set_ylabel("Attrition Count",fontweight="bold")
ax[2,0].legend(loc="lower left")
ax[2,0].grid()
ax[2,0].tick_params(axis="x",labelsize=6,rotation =90)
# environment Satisfaction Balance  attritions
Max_EnvironmentSatisfaction_attrition_values =Max_EnvironmentSatisfaction_attrition_values = EnvironmentSatisfaction_attrition.loc[
    EnvironmentSatisfaction_attrition["count"].idxmax(),
    "EnvironmentSatisfaction"
    ]
Max_EnvironmentSatisfaction_attrition_count =EnvironmentSatisfaction_attrition["count"].max()
mn_envir =[]
for satis in EnvironmentSatisfaction_attrition["count"]:
    if satis ==EnvironmentSatisfaction_attrition["count"].max():
        mn_envir.append("red")
    else:
        mn_envir.append("whitesmoke")

br=ax[2,1].bar(EnvironmentSatisfaction_attrition["EnvironmentSatisfaction"],EnvironmentSatisfaction_attrition["count"],edgecolor="black",color=mn_envir,label=" Minimum WorkLife Balance Attrition",width=0.3)
# ax[0,1].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[2,1].text(Max_EnvironmentSatisfaction_attrition_values,Max_EnvironmentSatisfaction_attrition_count,f"Maximum Environment Dissatisfaction Attrition:{Max_EnvironmentSatisfaction_attrition_count}",ha="center",va="bottom",color="red",fontweight ="bold",fontsize=8)
ax[2,1].set_title("Maximum Environment_Satisfaction Balance Attritions",fontweight ="bold",fontsize=12)
ax[2,1].set_xlabel("Environment Satisfactions",fontweight="bold")
ax[2,1].set_ylabel("Attrition Count",fontweight="bold")
ax[2,1].legend(loc="lower right")
ax[2,1].grid()
ax[2,1].tick_params(axis="x",labelsize=6,rotation =90)
# minimum Environment Satisifiction balance
Min_EnvironmentSatisfaction_attrition_values =EnvironmentSatisfaction_attrition["EnvironmentSatisfaction"].idxmin()
Min_EnvironmentSatisfaction_attrition_count =EnvironmentSatisfaction_attrition["count"].min()
mn_envir =[]
for satis in EnvironmentSatisfaction_attrition["count"]:
    if satis ==EnvironmentSatisfaction_attrition["count"].min():
        mn_envir.append("green")
    else:
        mn_envir.append("whitesmoke")

br=ax[2,2].bar(EnvironmentSatisfaction_attrition["EnvironmentSatisfaction"],EnvironmentSatisfaction_attrition["count"],edgecolor="black",color=mn_envir,label=" Minimum WorkLife Balance Attrition",width=0.3)
# ax[0,1].bar_label(br,padding=5,color="blue",fontweight="bold",fontsize=6)
ax[2,2].text(Min_EnvironmentSatisfaction_attrition_values,Min_EnvironmentSatisfaction_attrition_count,f"Minimum Environment Dissatisfaction Attrition:{Min_EnvironmentSatisfaction_attrition_count}",ha="center",va="bottom",color="green",fontweight ="bold",fontsize=8)
ax[2,2].set_title("Minimum Environment_Satisfaction Balance Attritions",fontweight ="bold",fontsize=12)
ax[2,2].set_xlabel("Environment Satisfactions",fontweight="bold")
ax[2,2].set_ylabel("Attrition Count",fontweight="bold")
ax[2,2].legend(loc="lower right")
ax[2,2].grid()
ax[2,2].tick_params(axis="x",labelsize=6,rotation =90)

plt.tight_layout()
plt.show()
# then find the business insights
total_attriiton=df["Attrition"].value_counts()
print(total_attriiton)

# then the Sales vs attrition (check the if salary increase then if Attrition will decrease) check
Attrition_Monthlyincome_max =df["MonthlyIncome"].value_counts().max()
Attrition_Monthlyincome_min =df["MonthlyIncome"].value_counts().min()
Attrition_Monthlyincome_average =df["MonthlyIncome"].value_counts().mean()
print("Check the Slary Vs Attrition",Attrition_Monthlyincome_max)
print("Check the Slary Vs Attrition",Attrition_Monthlyincome_min)
print("Check the Slary Vs Attrition",Attrition_Monthlyincome_average)

# attrition vs standadhourse
Attrition_Standardhourse =df.groupby("Attrition")["StandardHours"].value_counts()
print(Attrition_Standardhourse)
Attrition_Hourlyrate =df.groupby("Attrition")["HourlyRate"].value_counts().mean()
print(Attrition_Hourlyrate)
# //chech the promotion YearsSinceLastPromotion then check if the work year last promotion attition the company
YearsSinceLastPromotion_vs_Attrition =Yes_Attrition["YearsSinceLastPromotion"].value_counts()
print(YearsSinceLastPromotion_vs_Attrition)

# //YearsInCurrentRole
YearsInCurrentRole_attrtion =Yes_Attrition["YearsInCurrentRole"].value_counts()
print(YearsInCurrentRole_attrtion)


JobLevel_attrtion =Yes_Attrition["JobLevel"].value_counts()
print(JobLevel_attrtion)

MonthlyIncome_attrtion =Yes_Attrition["MonthlyIncome"].value_counts()
print(MonthlyIncome_attrtion)
StockOptionLevel_attrtion =Yes_Attrition["StockOptionLevel"].value_counts()
print(StockOptionLevel_attrtion)
percentagesalaryhike =Yes_Attrition["PercentSalaryHike"].value_counts()
print(percentagesalaryhike)
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="HR Attrition Predictor", layout="wide")

st.title("📊 HR Attrition Prediction Dashboard")

# =========================
# LOAD DATA (ASSUME df already loaded)
# =========================
# df = pd.read_csv("HR_Attrition.csv")

# =========================
# DATA PREPROCESSING
# =========================
la = LabelEncoder()
df["Attrition"] = la.fit_transform(df["Attrition"])

# Features
X = df[[
    "MonthlyIncome",
    "JobLevel",
    "PercentSalaryHike",
    "StockOptionLevel",
    "JobSatisfaction",
    "WorkLifeBalance",
    "EnvironmentSatisfaction"
]]

y = df["Attrition"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# =========================
# SIDEBAR INPUTS
# =========================
st.sidebar.header("Employee Input Panel")

monthly_income = st.sidebar.slider("Monthly Income", 1000, 20000, 5000)

job_level = st.sidebar.number_input("Job Level", 1, 5, 1)

salary_hike = st.sidebar.slider("Salary Hike %", 0, 50, 10)

stock_option = st.sidebar.number_input("Stock Option Level", 0, 3, 0)

# Extra options (expandable)
with st.sidebar.expander("More Factors"):
    job_satisfaction = st.slider("Job Satisfaction", 1, 5, 3)
    work_life_balance = st.slider("Work Life Balance", 1, 4, 2)
    distance = st.number_input("Distance From Home", 1, 30, 5)

# =========================
# MAIN UI
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", len(df))
col2.metric("Attrition Count", df["Attrition"].sum())
col3.metric("Avg Salary", round(df["MonthlyIncome"].mean(), 2))

# =========================
# PREDICTION SECTION
# =========================
st.subheader("🔮 Employee Attrition Prediction")

if st.button("Predict Attrition"):

    input_data = pd.DataFrame([[
        monthly_income,
        job_level,
        salary_hike,
        stock_option
    ]], columns=[
        "MonthlyIncome",
        "JobLevel",
        "PercentSalaryHike",
        "StockOptionLevel"
    ])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    # RESULT DISPLAY
    st.subheader("Result:")

    if prediction[0] == 0:
        st.success("✅ Employee WILL STAY in the company")
    else:
        st.error("❌ Employee WILL LEAVE the company")

    # RISK SCORE
    st.metric("Attrition Risk Score", f"{probability*100:.2f}%")

    # RISK LEVEL
    if probability > 0.7:
        st.warning("🔴 HIGH RISK EMPLOYEE")
    elif probability > 0.4:
        st.info("🟠 MEDIUM RISK EMPLOYEE")
    else:
        st.success("🟢 LOW RISK EMPLOYEE")

    # JSON OUTPUT
    st.json({
        "prediction": int(prediction[0]),
        "risk_probability": float(probability)
    })

# =========================
# DATA INSIGHTS SECTION
# =========================
st.subheader("📊 Quick Insights")

st.write("Attrition Distribution")
st.bar_chart(df["Attrition"].value_counts())

st.write("Monthly Income Distribution")
st.bar_chart(df["MonthlyIncome"])