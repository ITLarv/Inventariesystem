import PyQt5
import util


####### Storage #######
def storage_search(qt5):
    company = qt5.lineEdit_storage_company.text()
    try:
        id = util.companies_to_id(company)
        qt5.gui_func.updateStatus(window=qt5.textBrowser_storage, id=id)
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_storage, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_storage, message="Company could not be found")


def storage_checkin(qt5, db):
    try:
        company = qt5.lineEdit_storage_company.text()
        db.checkInCompany(util.companies_to_id(company))
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_storage, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_storage, message="Company could not be found")
    storage_search(qt5)

def storage_checkout(qt5, db):
    try:
        company = qt5.lineEdit_storage_company.text()
        db.checkOutCompany(util.companies_to_id(company))
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_storage, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_storage, message="Company could not be found")
    storage_search(qt5)


####### Palldragare #######
def storage_borrow(qt5, db):
    name = qt5.lineEdit_storage_name.text()
    palldragareId = qt5.comboBox_storage_borrow_id.currentText()
    if palldragareId == "":
        qt5.gui_func.guiPalldragare(window=qt5.textBrowser_storage)
        return 1
    if name == "":
        qt5.gui_func.guiPalldragare(window=qt5.textBrowser_storage, message="Need to fillout name!")
        return -1

    try:
        db.borrowPalldragare(name, palldragareId)
        qt5.gui_func.guiPalldragare(window=qt5.textBrowser_storage, message="Palldragare has sucessfully been borrowed")

        #qt5.comboBox_storage_borrow_id.setText("")
        qt5.comboBox_storage_borrow_id.setCurrentIndex(0)
        qt5.lineEdit_storage_name.setText("")
    except:
        qt5.gui_func.guiPalldragare(window=qt5.textBrowser_storage, message="Something went wrong with the palldragare")


def storage_return(qt5, db):
    palldragarId = qt5.comboBox_storage_return_id.currentText()
    if palldragarId == "":
        qt5.gui_func.guiPalldragare(window=qt5.textBrowser_storage)


    try:
        db.returnPalldragare(palldragarId)
        qt5.gui_func.guiPalldragare(window=qt5.textBrowser_storage)

        #qt5.comboBox_storage_return_id.setText("")
        qt5.comboBox_storage_return_id.setCurrentIndex(0)
    except:
        qt5.gui_func.guiPalldragare(window=qt5.textBrowser_storage, message="Something went wrong with the palldragare")


####### Transportation #######
def transportation_search(qt5):
    company = qt5.lineEdit_transportation_company.text()
    try:
        id = util.companies_to_id(company)
        qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, id=id)
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="Company could not be found")

def transportation_register(qt5, db):
    company = qt5.lineEdit_transportation_company.text()
    roomId = qt5.lineEdit_transportation_lokal.currentText()
    placement = qt5.lineEdit_transportation_id_plats.text()
    if placement == "":
        qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No platsid was given")
        return 0
    if roomId== "":
        qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No lokal was given")
        return 0
    try:
        companyId = util.companies_to_id(company)
        db.initGods(companyId, placement, roomId)
        qt5.lineEdit_transportation_id_plats.setText("")
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="Company could not be found")

    transportation_search(qt5)


def transportation_send(qt5, db):
    company = qt5.lineEdit_transportation_company.text()
    try:
        companyId = util.companies_to_id(company)

        db.sendGods(companyId)
        transportation_search(qt5)
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="Company could not be found")
    



### Kollin ###
def transportation_kollin_add(qt5, db):
    company = qt5.lineEdit_transportation_company.text()
    placement = qt5.lineEdit_transportation_id_plats.text()
    if placement == "":
        qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No platsid was given")
        return 0

    try:
        companyId = util.companies_to_id(company)
        db.addKollin(companyId, placement)
        transportation_search(qt5)
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="Company could not be found")


def transportation_kollin_return(qt5, db):
    company = qt5.lineEdit_transportation_company.text()
    placement = qt5.lineEdit_transportation_id_plats.text()
    if placement == "":
        qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No platsid was given")
        return 0

    try:
        companyId = util.companies_to_id(company)

        db.subKollin(companyId, placement)
        transportation_search(qt5)
    except:
        if company == "":
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="No company was given")
        else:
            qt5.gui_func.updateStatus(window=qt5.textBrowser_transportation, message="Company could not be found")


####### Furniture #######
def furniture_search(qt5):
    company = qt5.lineEdit_furniture_company.text()
    try:
        company_id = util.companies_to_id(company)
        qt5.gui_func.furniture(window=qt5.textBrowser_furniture_furniture, id=company_id)
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, id=company_id)
    except:
        if company == "":
            qt5.gui_func.furniture(window=qt5.textBrowser_furniture_furniture, message="No company was given")
            qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="No company was given")
        else:
            qt5.gui_func.furniture(window=qt5.textBrowser_furniture_furniture, message="Company could not be found")
def furniture_get(qt5, db):
    try:
        company = qt5.lineEdit_furniture_company.text()
        db.claimFurniture(util.companies_to_id(company))
        furniture_search(qt5)
    except:
        if company == "":
            qt5.gui_func.furniture(window=qt5.textBrowser_furniture_furniture, message="No company was given")
        else:
            qt5.gui_func.furniture(window=qt5.textBrowser_furniture_furniture, message="Company could not be found")

def furniture_return(qt5, db):
    try:
        company = qt5.lineEdit_furniture_company.text()
        db.returnFurniture(util.companies_to_id(company))
        furniture_search(qt5)
    except:
        if company == "":
            qt5.gui_func.furniture(window=qt5.textBrowser_furniture_furniture, message="No company was given")
        else:
            qt5.gui_func.furniture(window=qt5.textBrowser_furniture_furniture, message="Company could not be found")


def furniture_extra_add(qt5, db):
    company = qt5.lineEdit_furniture_company.text()
    if company == "":
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="No company was given")
        return 0
    furnitureType = qt5.comboBox_furniture_extra.currentText()
    if furnitureType == "":
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="Need to choose a furniture")
        return 0

    try:
        companyId = util.companies_to_id(company)
        db.addExtraFurniture(companyId, str(furnitureType))
        furniture_search(qt5)
    except:
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="Company could not be found")


def furniture_extra_return(qt5, db):
    company = qt5.lineEdit_furniture_company.text()
    if company == "":
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="No company was given")
        return 0
    furnitureType = qt5.comboBox_furniture_extra.currentText()
    if furnitureType == "":
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="Need to choose a furniture")
        return 0

    try:
        companyId = util.companies_to_id(company)
        db.returnExtraFurniture(companyId, str(furnitureType))
        furniture_search(qt5)
    except:
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="Company could not be found")
        
def furniture_extra_book(qt5, db):
    print("in bookingh")
    company = qt5.lineEdit_furniture_company.text()
    if company == "":
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="No company was given")
        return 0
    furnitureType = qt5.comboBox_furniture_extra.currentText()
    if furnitureType == "":
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="Need to choose a furniture")
        return 0

    try:
        companyId = util.companies_to_id(company)
        status = db.bookExtraFurniture(companyId, furnitureType)
        if status == -3:
            qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="No more furnitures of this type left")
        else:
            furniture_search(qt5)
    except:
        qt5.gui_func.extraFurniture(window=qt5.textBrowser_furniture_extra, message="Company could not be found")


####### Lack page #######
def lack_register(qt5, db):
    header = qt5.lineEdit_lack_company.text()
    text = qt5.lineEdit_lack_company_2.text()

    db.initComplaint(header, text)

    qt5.lineEdit_lack_company.setText("")
    qt5.lineEdit_lack_company_2.setText("")
    
    lack_update(qt5)


def lack_update(qt5):
    qt5.gui_func.updateComplaint(window=qt5.textBrowser_lack)


####### Lokal #######
def add_lokal_button(qt5, db):
    try:
        roomId = qt5.lineEdit_init_room_id.text()
        person = qt5.lineEdit_init_room_person.text()
        db.addLokal(roomId, person)
        qt5.lineEdit_init_room_id.setText("")
        qt5.lineEdit_init_room_person.setText("")
    except:
        pass


def remove_lokal_button(qt5, db):
    try:
        roomId = qt5.lineEdit_init_room_id.text()
        db.removeLokal(roomId)
        qt5.lineEdit_init_room_id.setText("")
        qt5.lineEdit_init_room_person.setText("")
    except:
        pass
