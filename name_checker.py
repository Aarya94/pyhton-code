#name checker
name = input("enter your name: ")
def name_check():
        global name

        if 1<=len(name)<=12:
            if " " not in name:
                if name.isalpha():
                    print("input saved")
                else:
                    name= input("enter name having alphabets only : ")
                    name_check()
            else:
                name=input("print name without space : ")
                name_check()
        else:
            name=input ("name should be of 12 character only : ")
            name_check()
name_check()
