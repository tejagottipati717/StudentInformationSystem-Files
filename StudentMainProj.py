from StudentMenu import menu
from StudentAdd import savestuddata
from StudentViews import getallrecords,getrecord
from StudentDelete import deleterecord
from StudentUpdate import Updaterecord
from StudentSearch import Searchrecord

while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                savestuddata()
            case 2:
                getallrecords()
            case 3:
                getrecord()
            case 4:
                deleterecord()

            case 5:
                Updaterecord()
            case 6:
                Searchrecord()
            case 7:
                print("Thx fo using the App")
                break
            case _:
                print("Ur Selection of operation is wrong---try again")
    except ValueError:
        print("Don't Enter Alnum's,Str's and Symbols")