contacts = []
def add_new_contact():
    name= input("name:")
    phone= input("phone:")
    email= input("email:")
    contact={"name":name,"phone":phone,"email":email}
    contacts.append(contact )
    print("contact saved",contact)
def view_contact():
    k=input("do you what to view your contact?")
    if k=="yes":
        print(contacts)
def search_for_contact():
    name= input(" name ?")
    for contact in contacts:
        if name==contact["name"]:
            print(contact)
def delete_contact():
    delete=(input("contact to delet"))
    for contact in contacts :
        if delete==contact['name']:
            contacts.remove(contact)
            print("contact deleted ")
def show_options():
    print("add new contact")
    print("deleted conact")
    print("view conact")
    print("search for conact")
    print("back")
while True:
    show_options()
    s=input("choose option") 
    if s=="add new contact": 
        add_new_contact() 
    elif s == "delete a contact": 
        delete_contact() 
    elif s== "view contacts": 
        view_contact() 
    elif s == "search for contact": 
        search_for_contact()
    elif s== "back":
     break