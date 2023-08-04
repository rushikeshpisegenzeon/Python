from Main_App.Input_Pack import user_inputs as u
from Main_App.Operations import Fetch_Data as f
from Main_App.Operations import Details_By_Id as d
from Main_App.Operations import Update_Name as n
while True:

    print('''
    1.Enter Students Details
    2.Fetch All Students Details
    3.Fetch Details By the ID
    4.Update the Name of Student
    5.Exit
    ''')

    ch = int(input("Enter Your Choice : "))
    if ch ==1:
        u.input_data()
    elif ch==2:
        f.display()
    elif ch==3:
        id=int(input("Enter the Id : "))
        d.By_Id(id)
    elif ch==4:
        id=int(input("Enter your Id : "))
        name=input("Enter your Good Name : ")
        n.updateName(id,name)
    elif ch==5:
        break