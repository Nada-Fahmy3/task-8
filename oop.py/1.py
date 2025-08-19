class Magical_contact:
    def _init_(self,name,email,phone_number):
        self.__name =name
        self.__email=email
        self.__phone_number=phone_number
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_phone_number(self):
        return self.__phone_number
    def set_email(self,email):
        self.__email=email
    def set_phone_number(self,phone_number):
        self.__phone_number=phone_number
    def describe(self):
        print(f"name: {self._name} email: {self.email}phone_number: {self._phone_number}")
class Wizard_or_witch(Magical_contact):
    def _init_(self,name,email,phone_number,wand,house):
        super()._init_(name,email,phone_number)
        self.__wand=wand
        self.__house=house
        houses=["gryfindor","hufflepuff","ravenclaw","slytherin"]
        if house in houses:
            None
        else:
            print("value error")
    def get_wand(self):
        return f"{self._wand['length']} ,{self.wand['core']},{self._wand['wood']}"
    def get_house(self):
        return self.__house
    def describe(self):
        print(f"name:{self.get_name()} email:{self.get_email()}phone_number:{self.get_phone_number()}wand:{self._wand}house:{self._house}")
class Magical_creature(Magical_contact):
    def _init_(self,name,email,phone_number,species,is_tame):
        super()._init_(name,email,phone_number)
        self.__species=species
        self.__is_tame=is_tame
    def get_species(self):
        return self.__species
    def is_tame (self):
        if self.__is_tame==True:
            return True
        else:
            return False
    def describe(self):
        print(f"name: {self.get_name()}email:{self.get_email()} phone_number:{self.get_phone_number()}species:{self._species}tame:{self._is_tame}")
class Magical_contact_book:
    def _init_(self):
        self.__contacts=[]
    def add_contact(self,contact):
        self.__contacts.append(contact)
    def list_contact(self):
        for contact in self.__contacts:
            contact.describe()
            print("")
    def find_contact(self,name):
        for contact in self.__contacts:
            if contact.get_name()==name:
             contact.describe()
g=Magical_contact_book()
nada=Magical_creature("nada","nada@mail","225563","hipoogrif",True)
g.add_contact(nada) 
g.list_contact()
g.find_contact("nada")