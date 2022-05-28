
import mysql.connector
import os
from dotenv import load_dotenv

class Mydatabase:
    def __init__(self):
        load_dotenv()
        self.PASSWORD = os.getenv('SQL_TOKEN')
        self.PORT = os.getenv('PORT')
        self.__mydb = mysql.connector.connect(
            host ="mysql80.r101.websupport.se",
            user = "itlog",
            password = self.PASSWORD, 
            port = self.PORT,
            database = "larvlog"   
        )
        self.__mycursor = self.__mydb.cursor()
    
    def updateDb(self):
        self.__mydb = mysql.connector.connect(
            host ="mysql80.r101.websupport.se",
            user = "itlog",
            password = self.PASSWORD, 
            port = self.PORT,
            database = "larvlog"   
        )
        self.__mycursor = self.__mydb.cursor()
        

    #========== Everything with companies ==========#
    # Add company
    def newCompany(self, companyId, comapnyName, storageId):
        #self.updateDb()
        try:
            sql = "INSERT INTO foretag (foretagsnummer, foretagsnamn, monterplats, status) VALUES ('" + str(companyId) + "', '" + comapnyName + "', '" + str(storageId) + "', 'Registrerad')"
            self.__mycursor.execute(sql)
            #self.__mydb.commit()
            return 1

        except mysql.connector.Error as error:
            print("Failed to insert company into MySQL table {}".format(error))
            return -1

    def commit(self):
        self.__mydb.commit()
        
    # Delete company
    def removeCompany(self, companyId):
        self.updateDb()
        try:
            sql = "DELETE FROM foretag WHERE foretagsnummer = '" + str(companyId) + "'"
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to delete company from MYSQL table {}".format(error))
            return -1

    # Returns registered companies
    def registeredCompanies(self, alt):
        self.updateDb()
        self.__mycursor.execute("SELECT * FROM foretag")
        result = self.__mycursor.fetchall()
        
        if alt == 1:
            returnList = []
            for x in result:
                returnList.append(x[1])
        if alt == 2:
            # This will return a dict: name:id
            returnList = {}
            for x in result:
                returnList[x[1]] = x[0]
        if alt == 3:
            # This will return a dict: id:name
            returnList = {}
            for x in result:
                returnList[int(x[0])] = x[1]

        return returnList

    # Return storaging for a company
    def monterSpace(self, companyId):
        self.updateDb()
        sql = "SELECT monterplats FROM foretag WHERE foretagsnummer = " + str(companyId)
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()

        return result[0][0] # [0][0] is just formating stuff

    # Set status of the company
    def checkInCompany(self, companyId):
        self.updateDb()
        try: 
            status = "Incheckad"
            sql = "UPDATE foretag SET status = \"" + str(status) + "\" WHERE foretagsnummer = " + str(companyId) 
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to update company status from MYSQL table {}".format(error))
            return -1

    def checkOutCompany(self, companyId):
        self.updateDb()
        try: 
            status = "Utcheckad"
            sql = "UPDATE foretag SET status = \"" + str(status) + "\" WHERE foretagsnummer = " + str(companyId) 
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to update company status from MYSQL table {}".format(error))
            return -1

    def getStatusCompany(self, companyId):
        self.updateDb()
        try:
            sql = "SELECT * FROM foretag WHERE foretagsnummer = " + str(companyId)  
            self.__mycursor.execute(sql)
            result = self.__mycursor.fetchall()
            return result[0][3]
        except mysql.connector.Error as error:
            print("Failed to get company status from MYSQL table {}".format(error))
            return -1
            


    #========== Everything with furniture ==========#
    # Main furniture
    def furnitureIsDeclared(self, furnitureType, companyId):
        self.updateDb()
        sql = "SELECT * FROM mobler WHERE (foretagsnummer = \"" + str(companyId) + "\" AND typ = \"" + str(furnitureType) + "\")"
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()
        return result != [] # Returns if furniture is declared

    def getInfoFurniture(self, furnitureType, companyId, searched):
        self.updateDb()
        sql = "SELECT " + searched +" FROM mobler WHERE (foretagsnummer = \"" + str(companyId) + "\" AND typ = \"" + str(furnitureType) + "\")"
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()
        return result[0][0] # Formating stuff [0][0]

    def initFurniture(self, furnitureType, companyId, antal):
        #self.updateDb()
        status = "Ej uthämtad"
        try:
            sql = "INSERT INTO mobler (typ, foretagsnummer, status, antal) VALUES ('" + str(furnitureType) + "', '" + str(companyId) + "', '" + str(status) + "', '" + str(antal) + "')"

            self.__mycursor.execute(sql)
            #self.__mydb.commit()
            return 1

        except mysql.connector.Error as error:
            print("Failed to init furniture into MySQL table {}".format(error))
            return 0


    # Function should either init or add furniture, depending if it already exists or not
    def claimFurniture(self, companyId):
        self.updateDb()
        # Get all furniture
        furniture = self.getAllFurniture(companyId)
        # Update each furniture to claimed
        sql = ""
        try:
            status = "Claimed"
            for e in furniture:
                furnitureType = e[0]
                sql = "UPDATE mobler SET status = \"" + str(status) + "\" WHERE (foretagsnummer = \"" + str(companyId) + "\" AND typ = \"" + str(furnitureType) + "\")"
                self.__mycursor.execute(sql)
                self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to claim furniture into MySQL table {}".format(error))
            return 0

    
    def returnFurniture(self, companyId):
        self.updateDb()
        # Get all furniture
        furniture = self.getAllFurniture(companyId)
        # Update each furniture to returned 
        try:
            status = "Returned"
            for e in furniture:
                furnitureType = e[0]
                sql = "UPDATE mobler SET status = \"" + str(status) + "\" WHERE (foretagsnummer = \"" + str(companyId) + "\" AND typ = \"" + str(furnitureType) + "\")"
                self.__mycursor.execute(sql)
                self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to return furniture into MySQL table {}".format(error))
            return 0

    def getAllFurniture(self, companyId):
        self.updateDb()
        sql = "SELECT * FROM mobler WHERE foretagsnummer = " + str(companyId) 
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()
        return result


    # Extra furniture
    def addExtraFurniture(self, companyId, furnitureType, nr=1):
        self.updateDb() # This is used because getInFuntiture() does not have the call
        old_status = self.getInfoFurniture(furnitureType, companyId, "status")
        antal = int(self.getInfoFurniture(furnitureType, companyId, "antal")) 
        if int(old_status) <= antal:
            # The limit is reached
            return -2
        else:
            # This is just adding numbers on a instance
            #sql = "UPDATE extramobler SET antal = '" + str(antal + 1) + "' WHERE (foretagsnummer = '" + str(companyId) + "' AND typ = '" + str(furnitureType) + "')"
            sql = "UPDATE extramobler SET antal = antal+1 WHERE (foretagsnummer = '" + str(companyId) + "' AND typ = '" + str(furnitureType) + "')"

        self.__mycursor.execute(sql)
        self.__mydb.commit()
        return 1
        
    def returnExtraFurniture(self, companyId, furnitureType, nr=1):
        self.updateDb() # This is used because getInFuntiture() does not have the call
        antal = int(self.getInfoFurniture(furnitureType, companyId, "antal")) - nr
        # Bounds check
        if antal < 0:
            return -3
        sql = "UPDATE extramobler SET antal = antal-1 WHERE (foretagsnummer = '" + str(companyId) + "' AND typ = '" + str(furnitureType) + "')"

        self.__mycursor.execute(sql)
        self.__mydb.commit()
        return 1
    
    def bookExtraFurniture(self, companyId, furnitureType, nr=1):
        self.updateDb() # This is used because getInFuntiture() does not have the call
        old_status = int(self.getInfoFurniture(furnitureType, companyId, "status"))
        totalFurniture = int(self.getInfoFurniture(furnitureType, "None", "status"))

        if old_status == 0 and totalFurniture > 0:
            sql = "INSERT INTO extramobler (typ, foretagsnummer, status, antal) VALUES ('" + str(furnitureType) + "', '" + str(companyId) + "', '1', '0')"
        else:
            if totalFurniture > 0:
                status = int(old_status) + 1
                sql = "UPDATE extramobler SET status = '" + str(status) + "' WHERE (foretagsnummer = '" + str(companyId) + "' AND typ = '" + str(furnitureType) + "')"
            else:
                return -3
        self.__mycursor.execute(sql)
        sql  = "UPDATE extramobler SET status = '" + str(totalFurniture-1) + "' WHERE (foretagsnummer IS NULL AND typ = '" + str(furnitureType) + "')"

        self.__mycursor.execute(sql)
        self.__mydb.commit()
        return 1

    def getAllExtraFurniture(self, companyId):
        self.updateDb()
        sql = "SELECT * FROM extramobler WHERE foretagsnummer = " + str(companyId) 
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()
        return result
    
    def initExtraFurniture(self, furnitureType, nr=1):
        self.updateDb()
        sql = "INSERT INTO extramobler (typ, foretagsnummer, status, antal) VALUES ('" + str(furnitureType) + "', NULL, '" + str(nr) + "', '0')"
        self.__mycursor.execute(sql)
        self.__mydb.commit()
        return 1


    ### OBSERVE, THIS FUNCTION DOES NOT IT DOES NOT UPDATE THE DB CONNECTION
    # If using this functin, you need to manually update with "self.updateDb()"
    # Reason is if collecting data many times from the database and reastablishing a connection to update will take time.
    # So if using this function the update can be called ONCE before and all the data is new.
    def getInfoFurniture(self, furnitureType, companyId, searched):
        if companyId == "None":
            sql = "SELECT * FROM extramobler WHERE (foretagsnummer IS NULL AND typ = '" + str(furnitureType) + "')"
 
        else:
            sql = "SELECT * FROM extramobler WHERE (foretagsnummer = '" + str(companyId) + "' AND typ = '" + str(furnitureType) + "')"

        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()

        if result == []:
            return 0
        if searched == "antal":
            return str(result[0][4])
        if searched == "status":
            return str(result[0][2])




    #========== palldragare ==========#
    # Borrow
    def borrowPalldragare(self, name, palldragarId):
        self.updateDb()
        try:
            sql = "INSERT INTO palldragare (palldragarnummer, namn) VALUES ('" + str(palldragarId) + "', '" + str(name) + "')"
            
            self.__mycursor.execute(sql)
            self.__mydb.commit()
        except mysql.connector.Error as error:
            print("Failed to insert palldragare into MySQL table {}".format(error))

    # Return
    def returnPalldragare(self, palldragarId):
        self.updateDb()
        try:
            sql = "DELETE FROM palldragare WHERE palldragarnummer = '" + str(palldragarId) + "'"

            self.__mycursor.execute(sql)
            self.__mydb.commit()
        except mysql.connector.Error as error:
            print("Failed to delete palldragare from MYSQL table {}".format(error))
    
    def allPalldragare(self):
        self.updateDb()
        self.__mycursor.execute("SELECT * FROM palldragare")
        result = self.__mycursor.fetchall()

        allPalldragare = []
        for x in result:
            allPalldragare.append(x)
        
        return allPalldragare
    
    #========== Lokal =========#
    def isLokal(self, roomId):
        self.updateDb()
        sql = "SELECT * FROM lokal WHERE salsnummer = " + str(roomId)
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()

        return result != []

    def updateLokal(self, roomId, person):
        self.updateDb()
        sql = "UPDATE lokal SET ansvarig = \"" + str(person) + "\" WHERE salsnummer = " + str(roomId)
        self.__mycursor.execute(sql)
        self.__mydb.commit()

    def addLokal(self, roomId, person):
        self.updateDb()
        try:
            if not self.isLokal:
                self.updateLokal(roomId, person)
            else:
                sql = "INSERT INTO lokal (salsnummer, ansvarig) VALUES ('" + str(roomId) + "', '" + str(person) + "')"
                self.__mycursor.execute(sql)
                self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to insert lokal into MySQL table {}".format(error))
            return -1
    
    def removeLokal(self, roomId):
        self.updateDb()
        try:
            sql = "DELETE FROM lokal WHERE salsnummer = '" + str(roomId) + "'"
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to delete lokal from MYSQL table {}".format(error))
            return -1
    
    def allLokal(self):
        self.updateDb()
        try:
            sql = "SELECT * FROM lokal"
            self.__mycursor.execute(sql)
            result = self.__mycursor.fetchall()
            return result
        except mysql.connector.Error as error:
            print("Failed to get lokal from MySQL table {}".format(error))
            return -1


    
    #========== Gods =========#
    def initGods(self, companyId, placement, roomId):
        self.updateDb()
        # Salsnummer och platsnummer måste checkas för skillnader etc.
        try:
            sql = "INSERT INTO gods (platsnummer, foretagsnummer, salsnummer, lagerstatus, kollins) VALUES ('" + str(placement) + "', '" + str(companyId) + "', '" + str(roomId) + "', 'Registrerad', '0')"
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to insert palldragare into MySQL table {}".format(error))
            return -1

    def sendGods(self, companyId):
        self.updateDb()
        try:
            sql = "UPDATE gods SET lagerstatus = \"Skickad\" WHERE foretagsnummer = " + str(companyId)
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to update gods status MySQL table {}".format(error))
            return -1

    def godsAllLocation(self, companyId):
        self.updateDb()
        try:
            sql = "SELECT  * FROM gods WHERE foretagsnummer = " + str(companyId)
            self.__mycursor.execute(sql)
            result = self.__mycursor.fetchall()
            locationTuple= [] 
            if result != []:
                for e in result:
                    locationTuple.append((str(e[0]), str(e[2])))
                return locationTuple
            return 0
        except mysql.connector.Error as error:
            print("Failed to get gods status from MYSQL table {}".format(error))
            return -1
        

    def removeGods(self, companyId):
        self.updateDb()
        sql = "DELETE FROM gods WHERE foretagsnummer = " + str(companyId)
        self.__mycursor.execute(sql)
        self.__mydb.commit()
        return 1

    
    def getStatusGods(self, companyId):
        self.updateDb()
        try:
            sql = "SELECT  * FROM gods WHERE foretagsnummer = " + str(companyId)
            self.__mycursor.execute(sql)
            result = self.__mycursor.fetchall()
            if result != []:
                return result[0][3]
            return ""
        except mysql.connector.Error as error:
            print("Failed to get gods status from MYSQL table {}".format(error))
            return -1

    def godsNr(self, companyId):
        self.updateDb()
        try:
            sql = "SELECT  * FROM gods WHERE foretagsnummer = " + str(companyId)
            self.__mycursor.execute(sql)
            result = self.__mycursor.fetchall()
            return len(result)
        except mysql.connector.Error as error:
            print("Failed to get company status from MYSQL table {}".format(error))
            return -1
        


    #========== Kollin =========#
    def getKollin(self, companyId, platsnummer):
        self.updateDb()
        try:
            sql = "SELECT * FROM gods WHERE (foretagsnummer = \"" + str(companyId) + "\" AND platsnummer = \"" + str(platsnummer) + "\")"
            self.__mycursor.execute(sql)
            result = self.__mycursor.fetchall()
            if result != []:
                return result[0][4]
            return 0
        except mysql.connector.Error as error:
            print("Failed to get company status from MYSQL table {}".format(error))
            return -1

    # This adds one kollin
    def addKollin(self, companyId, platsnummer):
        #self.updateDb() No need when having getKollin
        kollin = int(self.getKollin(companyId, platsnummer)) + 1

        try: 
            sql = "UPDATE gods SET kollins = \"" + str(kollin) + "\" WHERE (foretagsnummer = \"" + str(companyId) + "\" AND platsnummer = \"" + str(platsnummer) + "\")"
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to add kollin in MYSQL table {}".format(error))
            return -1

    # This subtracts one kollin
    def subKollin(self, companyId, platsnummer):
        #self.updateDb() No need when having getKollin
        kollin = int(self.getKollin(companyId, platsnummer)) - 1

        # Bounds check
        if kollin < 0:
            return 0

        try: 
            sql = "UPDATE gods SET kollins = \"" + str(kollin) + "\" WHERE (foretagsnummer = \"" + str(companyId) + "\" AND platsnummer = \"" + str(platsnummer) + "\")"
            self.__mycursor.execute(sql)
            self.__mydb.commit()
            return 1
        except mysql.connector.Error as error:
            print("Failed to add kollin in MYSQL table {}".format(error))
            return -1

    #========== Complaint =========#
    def initComplaint(self, header, text, companyId=None):
        self.updateDb()
        sql = "INSERT INTO felanmarkning (rubrik, text) VALUES ('"+ str(header) + "', '" + str(text) + "')"
        self.__mycursor.execute(sql)
        self.__mydb.commit()
        return 1

    def getAllComplaint(self):
        self.updateDb()
        sql = "SELECT * FROM felanmarkning"
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()
        return result

    #========== Testing area =========#

    # Prints all tables and a specified
    def descTable(self, table):
        self.updateDb()
        print("All tables:")
        self.__mycursor.execute("SHOW TABLES")
        for x in self.__mycursor:
            print(x)
        print()
        
        print(f"Desciption of {table}:")
        sql = "DESCRIBE " +  table
        self.__mycursor.execute(sql)
        result = self.__mycursor.fetchall()
        for x in result:
            print(x)
        print("\n")

    # This will print all instances of a specified table
    def printAll(self, what):
        self.updateDb()
        self.__mycursor.execute("SELECT * FROM " + str(what))
        result = self.__mycursor.fetchall()

        print("Alla", what)
        for x in result:
            print(x)
    
    def removeEverything(self):
        allStuff = ["extramobler", "felanmarkning", "mobler", "gods", "lokal", "palldragare", "foretag"]
        
        # Just do this for all in allStuff
        for e in allStuff:
            sql = "DELETE FROM " + e 
            self.__mycursor.execute(sql)

        self.__mydb.commit()
        print("Everything is deleted!!!")

    #========= Type the test in this function =========#
    def test(self): # This is the function that is run when testing this file
        self.descTable("extramobler")
        #self.removeEverything()
        #print(self.getInfoFurniture("Barstol", "None", "status"))
        #self.bookExtraFurniture(22, "Ståbord")

        #self.printAll("extramobler")

        

if __name__ == "__main__":
    import test