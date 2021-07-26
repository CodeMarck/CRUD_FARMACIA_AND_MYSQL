import mysql.connector

class Countries:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost",
            user="root",
            password="1523",
            port="3306",
            database="telesaludfarmacia"
        )

    def __str__(self):
        datos=self.consulta_paises()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def consulta_paises(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM adm")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_pais(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM adm WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_pais(self,Nombre, Tipo, Cantidad, Unidades):
        cur = self.cnn.cursor()
        sql='''INSERT INTO adm (nombre, tipo, cantidad, unidades) 
        VALUES('{}', '{}', '{}', '{}')'''.format(Nombre, Tipo, Cantidad, Unidades)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_pais(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM adm WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_pais(self,Id, Nombre, Tipo, Cantidad, Unidades):
        cur = self.cnn.cursor()
        sql='''UPDATE adm SET nombre='{}', tipo='{}', cantidad='{}',
        unidades='{}' WHERE Id={}'''.format(Nombre, Tipo, Cantidad, Unidades,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
