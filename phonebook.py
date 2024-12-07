def add():
    phonebook=open("contact.txt","a")
    name=input("Enter Name :")
    Number=int(input("Enter Phone Number :"))
    phonebook.write(name+"  :  "+str(Number))
    phonebook.close()


def search():
    phonebook=open("contact.txt","r")
    contact_data=input("Enter data to fetch :")
    for data in phonebook:
        if contact_data in data:
            print(data)
            break
    else:
            print("No Contact Found")
    phonebook.close()

def update():
    phonebook=open("contact.txt","r")
    lis=phonebook.readlines()
    update_date=input("Enter incorrect contact Name or Number  :")
    for data in range(len(lis)):
        if update_date in lis[data]:
            lis[data]=input("Enter Name :")+"  :   "+str(int(input("Enter Number :")))+"\n"
            break
    else:
        print("No Contact Found")
    phonebook.close()
    phonebook=open("contact.txt","w")
    phonebook.writelines(lis)
    phonebook.close()

def delete():
    phonebook=open("contact.txt","r")
    lis=phonebook.readlines()
    delete_data=input("Enter delete contact :")
    for data in lis:
        if delete_data in data:
            lis.remove(data)
            break
    else:print("No Contact Found")
    phonebook.close()
    phonebook=open("contact.txt","w")
    phonebook.writelines(lis)
    phonebook.close()
