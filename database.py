from sqlite3 import *

veza = connect("kalendar_događaja.db")

k = veza.cursor()

k.execute("CREATE TABLE IF NOT EXISTS događaji(naziv_događaja TEXT, datum_događaja TEXT, opis_događaja TEXT)")


veza.close()
