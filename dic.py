global db
db={}
def newuser():
    prompt='login desired: '
    while True:
        name=input(prompt)
        if name in db.keys():
            prompt='name taken,try another:'
            continue
        else:
            break
    pwd=input("please input the password:")
    db[name]=pwd
def olduser():
    name=input("login:")
    pwd=input("password")
    passwd=db.get(name)
    if pwd==passwd:
        print("welcome:")
    else:
        print("login again")
def showmenu():
    prompt="""
    (N)ew USer Login
    (O)lduser
    (Q)uit
    Enter Choice:"""
    while True:
        try:
            choice=input(prompt).strip()[0].lower()
        except(EOFError,KeyboardInterrupt,ValueError,TypeError):
            choice='q'
        if choice=='n':
            newuser()
        elif choice=='e':
            olduser()
        elif choice=='q':
            break
        else:
            print("Try again")
if __name__ == '__main__':
    showmenu()