signups = [("Liam", "Science"),("Emma", "Art"),("Olivia", "Science"),
    ("Liam", "Art"), ("Noah", "Art"),("Emma", "Science")]

science_club = set()  
art_club = set()      
seen_students = set()  

for name, club in signups:
    if name not in seen_students:  
        seen_students.add(name)     
        if club == "Science":
            science_club.add(name)  
        elif club == "Art":
            art_club.add(name)     

print("Science Club Members:", science_club)
print("Art Club Members:", art_club)
