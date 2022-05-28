import database
import csv
rows = []

with open("csv/furniture.csv", 'r', encoding="UTF-8") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    header[7] = header[7].replace("\"", "")
    for row in csvreader:
        if row[0] == "":
            break
        if row[1] != "":
            rows.append(row)


#print(*rows, sep="\n")

db = database.Mydatabase()
db.updateDb()

# This initializes all the companies
for e in range(len(rows)):
    db.newCompany(e, rows[e][0], rows[e][1])
    #print(e, rows[e][0], rows[e][1])

# For initialize all furniture
for i in range(len(rows)):
    for j in range(2, len(header)):
        if rows[i][j] != "" and rows[i][j] != "0" and rows[i][j] != "-" and rows[i][j] != 0 and rows[i][j] != " ":
            db.initFurniture(header[j], i, rows[i][j]) 
            #print(rows[i][0], header[j], rows[i][j])

db.commit()

db.initExtraFurniture("Barstol", 15)
db.initExtraFurniture("Ståbord", 15)

print("done")