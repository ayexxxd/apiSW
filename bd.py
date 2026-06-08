import mysql.connector

def get_db_connection():
    conexion = mysql.connector.connect(
    host="mysql-16922fc3-tec-00e9.k.aivencloud.com",
    user="avnadmin",
    password="AVNS_RWewn6VsGT1Znlvf84I",
    database="LuminaReto",
    port=17283)
    return conexion
