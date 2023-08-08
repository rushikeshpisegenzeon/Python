import sqlite3
from Main_Pack.User_Input import Adding_Patient_Details as p
from Main_Pack.User_Input import Adding_Medication as m
from Main_Pack.Operations.Display import All_Medications as am, All_Patients as a, All_Records as records
from Main_Pack.User_Input import Adding_Record as ar
from Main_Pack.Operations.Delete import delete_patient as dlp
from Main_Pack.Operations.Delete import delete_medication as dlm
from Main_Pack.Operations.update import update_patient as up
from Main_Pack.Operations.find_by import patient_record_by_id as pri
from Main_Pack.Operations.find_by import patients_by_disease as fd
from Main_Pack.Operations.update import update_medication as um
conn = sqlite3.connect('Medication_Management.db')

while True:

    print("\n==== Medication Management System ====")
    print("1. Add Patient")
    print("2. Display all Patients")
    print("3. Add Medications")
    print("4. Display all Medications")
    print("5. Delete a Patient")
    print("6. Delete Medication")
    print("7. Update Patient Details")
    print("8. Update Medication Details")
    print("9. Find Patient Records")
    print("10. Find Patients By Disease")
    print("11. Add Records")
    print("12. Display All Records")
    print("0. Exit")

    choice = input("Enter your choice: \n")
    if choice == "1":    #Add Patient details for new patient
        p.patient_details()
    elif choice == "2":  #Display all Patients details
        a.display()
    elif choice == "3":  #Add Medications when new medication comes to enter in list
        m.medication_details()
    elif choice == "4":  #Display all Medications details
        am.display()
    elif choice == "5":  # Delete a Patient by perticular Id
        p_id = input("Enter the Patient Id which you want to delete: ")
        dlp.del_patient(p_id)
    elif choice == "6":  # Delete a Medication by perticular Id
        m_id = input("Enter the medication Id which you want to delete: ")
        dlm.del_medication(m_id)
    elif choice == "7":  #update pateint details if u want to change perticular thing or whole data
        while True:
            print("1. Change Patients Name")
            print("2. Change Age")
            print("3. Change Gender")
            print('4. Exit')

            ch = int(input("Enter your choice: \n"))
            if ch!=4:
                p_id = int(input("Enter the patient Id: "))
            if ch==1:  #Update Patients Name
                new_name = input("Enter your good name: ")
                up.update_pname(p_id,new_name)
            elif ch==2: #Update age info
                new_age = int(input("Enter your right age: "))
                up.update_page(p_id, new_age)
            elif ch==3: #Update your gender
                new_gender = input("Enter your correct gender: ")
                up.update_pgender(p_id, new_gender)
            elif ch==4:
                print("Exit")
                break
            else:
                print("Invalid choice please enter right choice!")
    elif choice == "8":
         while True:
             print("1. Change medication name")
             print("2. Change disease name")
             print("3. Change the amount of dosage")
             print("4. change the frequency")
             print("5. Change the start Date")
             print("6. Change the End Date")
             print("7. Exit")

             ch = int(input("Enter your choice: \n"))
             if ch != 7:
                 m_id = int(input("Enter the medication Id: "))
             if ch==1: #update medication name
                 new_name=input("Enter the new medication name: ")
                 um.update_mname(m_id,new_name)
             elif ch==2: #update disease name
                 changed_disease_Name = input("Enter the updated disease: ")
                 um.update_disease(m_id,changed_disease_Name)
             elif ch==3: #update amout of dosage to patient
                 new_dosage = int(input("Enter the new amount of dosage: "))
                 um.update_dosage(m_id,new_dosage)
             elif ch==4: #update frequency of dose
                 new_frequency=input("Enter new frequency of medicine: ")
                 um.update_frequency(m_id,new_frequency)
             elif ch==5: #update date
                 new_date = input("Enter the new date in format yyyy-mm-dd: ")
                 um.update_startDate(m_id,new_date)
             elif ch==6: #update date
                 new_date = input("Enter the new date in format yyyy-mm-dd: ")
                 um.update_endDate(m_id, new_date)
             elif ch==7:
                 break
             else:
                 print("Enter the right choice please.")

    elif choice == "9": #find records - which will show you the all records of given patient Id
        p_id = int(input("Enter the patient Id: "))
        pri.find_by_id(p_id)
    elif choice == "10": #list out the all patients which have same disease
        disease_to_find = input("Enter the disease name: ")
        fd.find_patients_with_common_disease(disease_to_find)
    elif choice == "11": #add new record in the system
        p_id = int(input("Enter the patient Id: "))
        m_id = int(input("Enter the medication Id: "))
        ar.insert_record(p_id,m_id)
    elif choice == "12": #all the records in the system
         records.display_records()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please Enter right choice.")

