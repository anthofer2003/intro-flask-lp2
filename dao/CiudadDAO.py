# Data access object - DAO

from conexion.Conexion import Conexion

class CiudadDao:

    def getCiudades(self):

        CiudadSQL = """
        SELECT id, descripcion
        FROM ciudades 
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
         cur.execute(CiudadSQL)  
         lista_ciudades = cur.fetchall()
         return lista_ciudades 
        except con.Error as e:
            print(e)
        finally:
            cur.close()
            con.close()
        

    def guardarCiudad(self. descripcion):
       
       insertCiudadSQL = """
       INSERT INTO ciudades(descripcion:) 