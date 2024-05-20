import sqlite3

class Conexion:
  def __init__(self,nombre_bd):
    self.conexion=sqlite3.connect(nombre_bd)
    self.cursor=self.conexion.cursor()
  def crear_tabla_cliente(self):
    self.cursor.execute("CREATE TABLE IF NOT EXISTS cliente(nombre TEXT, apellido TEXT, dni TEXT)")
    self.conexion.commit()
  def agregar_cliente(self,nombre,apellido,dni):
    self.cursor.execute("INSERT INTO cliente VALUES(?,?,?)",(nombre,apellido,dni))
    self.conexion.commit()  
  def mostrar_clientes(self):
    cursor.execute("SELECT * FROM cliente")
    clientes=cursor.fetchall()
    return clientes
  