#%%
import sqlite3

con=sqlite3.connect("data.db")
kur=con.cursor()
class DataBase():
    def __init__(self):
        kur.execute("CREATE TABLE IF NOT EXISTS Kompyuter (id INTEGER,nomi TEXT,narxi REAL)")
        con.commit()
    def insert_table(self,a,b,c):
        kur.execute("INSERT INTO Kompyuter VALUES (?,?,?)",(a,b,c))
        con.commit()
    def show_info(self):
        kur.execute("SELECT nomi,narxi FROM Kompyuter")
        for i in kur.fetchall():
            print(*i)
    def drop_table(self):
        kur.execute("DROP TABLE Kompyuter")
        con.commit()
    def delete_info(self,name):
        kur.execute("DELETE FROM Kompyuter WHERE narxi=?",(name,))
        con.commit()
    def update_info(self):
        kur.execute("UPDATE Kompyuter SET nomi='Mac' WHERE nomi='HP'")
        kur.execute("UPDATE Kompyuter SET narxi=5000 WHERE narxi=2000")
ob=DataBase()
#ob.insert_table(1,"Acer",5000)
#ob.delete_info(input("Narxi: "))
ob.update_info()
ob.show_info()
#ob.drop_table()
con.close()
#%% MASALA
import sqlite3

con=sqlite3.connect("data.db")
kur=con.cursor()
class DataBase():
    def __init__(self):
        kur.execute("CREATE TABLE IF NOT EXISTS Oquvchi (id INTEGER,ism TEXT,family TEXT,yosh INTEGER)")
        con.commit()
    def insert_table(self,a,b,c,d):
        kur.execute("INSERT INTO Oquvchi VALUES (?,?,?,?)",(a,b,c,d))
        con.commit()
    def show_info(self):
        kur.execute("SELECT * FROM Oquvchi")
        for i in kur.fetchall():
            print(*i)
    def update_info(self):
        kur.execute("SELECT * FROM Oquvchi")
        list1=list()
        list2=list()
        for i in kur.fetchall():
            if i[0]%2==0:
                list2.append(i)
            else:
                list1.append(i)
        print(len(list1))
        kur.execute("DELETE FROM Oquvchi ")
        
        for i in range(len(list1)):
            self.insert_table(list2[i][0],list2[i][1],list2[i][2],list2[i][3])
            self.insert_table(list1[i][0],list1[i][1],list1[i][2],list1[i][3])
    def delete_info(self,name):
        kur.execute("DELETE FROM Kompyuter WHERE narxi=?",(name,))
        con.commit()
ob=DataBase()
while True:
    n=int(input("1-Malumot kiritish\n2-Malumot chiqarish\n3-Malumot almashtirish\n4-Malumot oshirish\n0-VIXOD\n>>>> "))
    if n == 1:
        n=int(input("Neshta malumot kiritasiz: "))
        for i in range(1,n+1):
            ob.insert_table(i,input(f"{i} Oquvchi ismi: "),input(f"{i} Oquvchi family: "),int(input(f"{i} Oquvchi yoshi: ")))
    elif n == 3:
        ob.update_info()
    elif n == 2:
        ob.show_info()
    elif n == 4:
        ob.delete_info(input("Oquvchi ismi: "))
    elif n == 0:
        break

#ob.drop_table()
con.close()
#%%
import sqlite3

con=sqlite3.connect("data.db")
kur=con.cursor()
class DataBase():
    def __init__(self):
        kur.execute("CREATE TABLE IF NOT EXISTS Dorxona (Nomi TEXT,Narxi REAL)")
        con.commit()
    def insert_table(self,a,b,c,d):
        kur.execute("INSERT INTO Dorxona VALUES (?,?)",(a,b))
        con.commit()
    def show_info(self):
        kur.execute("SELECT * FROM Dorxona")
        for i in kur.fetchall():
            print(*i)
    def update_info(self,a,b):
        kur.execute("SELECT * FROM Dorxona")
        list1=list()
        list2=list()
        for i in kur.fetchall():
            list2.append(i[0])
            list1.append(i[1])
        print(list2)
        for i in range(len(list2)):
           
            if list2[i] == a:
                
                kur.execute("UPDATE Dorxona SET  Narxi=? WHERE Narxi=?",(b,list1[i]))
                
    def delete_info(self,name):
        kur.execute("DELETE FROM Dorxona WHERE nomi=?",(name,))
        con.commit()
ob=DataBase()
while True:
    n=int(input("1-Malumot chiqarish\n2-Malumot almashtirish\n3-Malumot oshirish\n0-VIXOD\n>>>> "))
    if n == 2:
        ob.update_info(input("Nomi: "),int(input("Narxi: ")))
    elif n == 1:
        ob.show_info()
    elif n == 3:
        ob.delete_info(input("Oquvchi ismi: "))
    elif n == 0:
        break

#ob.drop_table()
con.close()


