import psycopg2 

class Conexion:

    """Metodo constructor de tu perro
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=anthofer password=fervaldez2003")

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con