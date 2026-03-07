def main():
    """data example made by chatgpt"""
    data = [ 
    {"name": "Ahmet", "age": 25, "skills": ["Python", "Java"]},
    {"name": "Mehmet", "age": None, "skills": []},         # age None
    {"age": 30, "skills": ["C++"]},                        # name eksik
    42,
    {"name": "Ayşe", "age": 30, "skills": ["Go"]},
    "random_text",
    {"name": "Ali", "age": 19, "skills": ["JavaScript"], "address": {"city": "İstanbul"}},
    {"name": "Zeynep", "age": 22},
    {"age": 27, "projects": [{"title": "Web App"}]},       # name eksik
    {"name": "Elif", "age": "", "skills": ["Java"]},       # age boş string
    3.14,
    ["nested", "list"],
    None,
    {"name": "Okan", "age": 28, "skills": ["C#", "Unity"], "address": {"city": "Bursa", "zip": "16000"}},
    {"name": "Merve", "age": 23, "projects": [{"title": "ML Model"}]},
    {"name": "", "age": 21, "skills": ["Rust"]},           # name boş string
    {"name": "Can"}                                       # age eksik
]
    fonk(*data)

def fonk(*args):
    clean_dict=[p for p in args if isinstance(p,dict) and p.get("name") and p.get("age") and (p["name"][0]=="A" or p["age"]>20)]
    for person in clean_dict:
        print(person["name"],"\nYas:",person["age"])
        if person.get("skills"):
            print("Yetenekler:",*person["skills"])
        else:
            print("Bilinen bir yetenegi yok")
        if person.get("projects"):
            print("Projeleri:",person["projects"][0]["title"])
        else:
            print("Bilinen bir projesi yok")
        if person.get("address"):
            print("Adresi:",*person["address"].values())
        else:
            print("Bilinen bir adresi yok")
        print("------------------------------")
if __name__=="__main__":
    main()