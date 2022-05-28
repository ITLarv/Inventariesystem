
####### lists #######
def all_furniture():
    return ["", "Ståbord", "Ståbordsöverdrag, vit", "Bord", "Barstol", "Klaffstol, svart", "Klaffstol stoppad sits, svart", "Miljöväxt", "TV-monitor 42\"", "TV-ställ"]


def all_extra_funiture():
    return ["", "Ståbord", "Barstol"]

def all_palldragare():
    return ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def all_companies():
    returnlist = []
    comp_and_id = companies_id()
    for key, val in comp_and_id.items():
        returnlist.append(key)
    # Will get all values from companies_id
    return returnlist

def all_registered_companies(db):
    # Will get all companies from database
    #return ["Annat företag", "yes"]
    return db.registeredCompanies(1)

def all_lokal(db):
    returnlist = []
    lokal_and_stuff = db.allLokal()
    for e in lokal_and_stuff:
        returnlist.append(e[0])
    return returnlist



####### dicts ######
def companies_id():
    import database
    db = database.Mydatabase()

    return db.registeredCompanies(2) 

def id_companies():
    import database
    db = database.Mydatabase()

    return db.registeredCompanies(3)

def companies_to_id(company):
    comanies = companies_id()
    return comanies[company]

def id_to_company(id):
    ids = id_companies()
    return ids[int(id)]


####### display formating ######
def color_text(statement):
    if statement == 0:
        return "font-size:14pt; color:#ff0000;" # Red
    if statement == 1:
        return "font-size:14pt; color:#00aa00;" # Green
    if statement == 2: 
        return "font-size:14pt; color:#0000FF;" # Blue 
    if statement == 3: 
        return "font-size:14pt; color:#BF40BF;" # Purple





