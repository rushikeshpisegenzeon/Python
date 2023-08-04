# import Main_App.Input_Pack.user_inputs as u
from Main_App.Input_Pack import user_inputs as u
from Main_App.Operations import fetch_records as f
from Main_App.Operations import fetch_by_branch as b
from Main_App.Operations import change_name as c
while True:

    print("-----MENU----")
    print('''
    1.Enter Participants Details
    2.Fetch Details
    3.Fetch participant by branch
    4.Update Wrongly entered name change
    5.Exit
    
    ''')
    ch = int(input("Enter Choice:-"))
    if ch == 1:
        u.input_data()
    elif ch==2:
        f.display()
    elif ch == 3:
        input_branch = input("Enter branch name:-")
        b.get_by_branch(input_branch)

    elif ch == 4:
        id,name = input("Enter ID , Correct name").split(",")
        c.update_name(int(id),name)
    else:
        break
