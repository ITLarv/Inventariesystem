import util
from PyQt5 import QtCore

class Gui_functions:
    def __init__(self, gui):
        self.gui = gui

    # This function is used for the display in the status windows.
    # Example of usage is to see the company stats, but also if there is any errors
    def updateStatus(self, window=None, id=None, message=None):
        _translate = QtCore.QCoreApplication.translate
        html_part = "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
        html_part_new = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
        default_color = "font-size:14pt; color:#000000"
        templateIsh = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">"
        # If there is no message
        if message == None:
            # If there is no id
            if id == None:
                # Here it will just print a empty window, nothing fancy
                # Usage of default color and everything default
                window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                + self.html_line(line="Företag")
                + self.html_line(line="Incheckad")
                + self.html_line(line="Lagerplats")
                + self.html_line(line="Kollin")
                + self.html_line(line="Status")
                + "</body></html>"))
            else:
                # This will print all the info of the current company in scope
                isCheckedIn = str(self.gui.db.getStatusCompany(id)) == "Incheckad"
                gods_status = str(self.gui.db.getStatusGods(id))
                if gods_status == "Skickad":
                    gods_color = 1
                elif gods_status == "Registrerad":
                    gods_color = 2
                elif gods_status == "":
                    gods_color = 0
                else:
                    gods_color = 3

                window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                + templateIsh + "Företag: " + util.id_to_company(id) + "</span></p>\n"
                + html_part_new + util.color_text(int(isCheckedIn)) + "\">Incheckad: " + str(isCheckedIn) + "</span></p>\n"
                + templateIsh + "Monterplats: " + str(self.gui.db.monterSpace(id)) + "</span></p>\n"
                + templateIsh + "------------</span></p>\n"
                + templateIsh + "Lagerinformation:</span></p>\n"
                + html_part_new + util.color_text(gods_color) + "\">Status: " + gods_status + "</span><p>\n"
                + templateIsh + "Gods: " + str(self.gui.db.godsNr(id)) + "</span></p>\n"
                + templateIsh + "Godsplatser: </span></p>\n"
                + self.godsLocation(self.gui.db, id)
                + "</body></html>"))


        else:
            # This is where the message is sent from, will desplay the text
            # This should probably be used for error message and stuff like that
            window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" " + html_part + "\"><span style=\" " + default_color + "\">" + message + "</span></p>\n"
                "</body></html>"))

    def furniture(self, window=None, id=None, message=None):
        _translate = QtCore.QCoreApplication.translate
        html_part = "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
        default_color = "font-size:14pt; color:#000000"
        # This function should look up all the furniture
        # Then render over all furniture and then add all the different furniture that has been borrowed
        if message != None:
            window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" " + html_part + "\"><span style=\" " + util.color_text(0) + "\">" + message + "</span></p>\n"
                "</body></html>"))
            return 1

        if id != None:
            templateIsh = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">"
            allFurniture = self.gui.db.getAllFurniture(id)
            add_html = templateIsh + "Företag: " + util.id_to_company(id) + "</span></p>\n"
            for e in allFurniture:
                add_html += templateIsh + str(e[0]) + " " + str(e[4]) + "st : " + str(e[2]) + "<br></span></p>\n"
            
            window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                + add_html +
                "</body></html>"))

            self.active_id_furniture = id
            self.active_window_furniture = window
            return 1
        return -1

    
    def extraFurniture(self, window=None, id=None, message=None):
        _translate = QtCore.QCoreApplication.translate
        html_part = "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
        default_color = "font-size:14pt; color:#000000"
        # This function should look up all the furniture
        # Then render over all furniture and then add all the different furniture that has been borrowed
        if message != None:
            window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" " + html_part + "\"><span style=\" " + util.color_text(0) + "\">" + message + "</span></p>\n"
                "</body></html>"))
            return 1

        if id != None:
            templateIsh = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">"
            allFurniture = self.gui.db.getAllExtraFurniture(id)
            add_html = templateIsh + "Kvar i lager: <br>Ståbord: " + str(self.gui.db.getInfoFurniture("Ståbord", "None", "status")) + "<br>Barstol: " + str(self.gui.db.getInfoFurniture("Barstol", "None", "status")) + "<br>---------------------<br></span></p>\n"
            add_html += templateIsh + "Företag: " + util.id_to_company(id) + "</span></p>\n"
            for e in allFurniture:
                add_html += templateIsh + str(e[0]) + ": " + str(e[4]) + " av " + str(e[2]) + "<br></span></p>\n"
            
            window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                + add_html +
                "</body></html>"))

            return 1
        return -1


    def updateComplaint(self, window, message=None):
        _translate = QtCore.QCoreApplication.translate
        html_ending = "</span></p>\n"
        templateIsh = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">"
        allComplaint= self.gui.db.getAllComplaint()
        allComplaint.reverse()
        html_content = ""
        for complaint in allComplaint:
            html_content += templateIsh + complaint[2] + html_ending 
            html_content += templateIsh + complaint[3] + html_ending 
            html_content += templateIsh + "--------------------------------------------" + html_ending 

        window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            + html_content +
            "</body></html>"))

    def guiPalldragare(self, window, message=None):
        _translate = QtCore.QCoreApplication.translate
        html_ending = "</span></p>\n"
        html_part = "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
        default_color = "font-size:14pt; color:#000000"
        templateIsh = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">"
        if message != None:
            window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" " + html_part + "\"><span style=\" " + default_color + "\">" + message + "</span></p>\n"
                "</body></html>"))
            return 1

        allPalldragare= self.gui.db.allPalldragare()
        html_content = ""
        for palldrare in allPalldragare:
            html_content += templateIsh + "palldragare " + palldrare[0] + ": " + palldrare[1] + html_ending 
            html_content += templateIsh + "--------------------------------------------" + html_ending 

        window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            + html_content +
            "</body></html>"))

   # This is the start for making the "updateStatus" more readable 
    def html_line(self, id=None, line=None):
        html_part_new = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
        templateIsh = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">"

        if id == None:
            return templateIsh + line + ": </span></p>\n"

        # From this here this function is not in use right now
        if line == "Företag":
            return templateIsh + "Företag: " + util.id_to_company(id) + "</span></p>\n"
        elif line == "Registrerad":
            return html_part_new + util.color_text(util.isRegisterd(self.gui.db, id)) + " \">Registrerad: " + str(util.isRegisterd(self.gui.db, id)) + "</span></p>\n"
    
    def godsLocation(self, db, id):
        html_ending = "</span></p>\n"
        templateIsh = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">"
        allLokal = db.godsAllLocation(id)
        returnString = ""
        if allLokal == 0:
            return ""
        for godsSpcae in allLokal:
            kollin = db.getKollin(id, godsSpcae[0])
            returnString += templateIsh + "Lokal: " + godsSpcae[1] + ", Platsnummer: " + godsSpcae[0] + ", Kollin: " + str(kollin) + html_ending 

        return returnString 

    
