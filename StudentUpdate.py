#StudentUpdate.py<-----------File Name and Module Name
import pickle
from StudentAdd import validation,InvalidNameError,ZeroLengthError,SpaceNameError
def Updaterecord():
    try:
        with open("NIT.data","rb") as rp:
            records=list()
            while(True):
                try:
                    record=pickle.load(rp)
                    records.append(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File Does not Exist")
    #Out-off 'with open() as ' Indentation
    # Accept the student Number  for updating sname and marks
    try:
        sno = int(input("Enter Student Number to Update the Record:"))
        found = False
        for i in range(len(records)):
            if(records[i][0]==sno):
                recno=i
                #records[i][1]=input("Enter New Name for Updating its Old Name:")
                #records[i][2]=float(input("Enter New Marks for Updating its Old Marks:"))
                found=True
                break
        if(found):
            records[recno][1] = validation(input("Enter New Name for Updating its Old Name:"))
            records[recno][2] = float(input("Enter New Marks for Updating its Old Marks:"))
            with open("NIT.data","wb") as fp:
                for record in records:
                    pickle.dump(record,fp)
            print("Student Record Updated Sucessfully")
        else:
            print("Record does not Exist")
    except ValueError:
        print("Don't enter alnums, strs and symbols for sno,marks")
    except InvalidNameError:
        print("Invalid Name--Try Again")
    except ZeroLengthError:
        print("Try to enter Ur Name")
    except SpaceNameError:
        print("Don't enter Space for Ur Name--try again:")