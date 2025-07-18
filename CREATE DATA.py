import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")
k = koneksi_ke_DB.cursor()

k.execute("""
INSERT INTO TBCars (
    id,
    name,
    brand,
    model,
    price
) VALUES (
    101,
    'Red Car',
    'Honda',
    'Civic',
    12000
)
""")

koneksi_ke_DB.commit()
koneksi_ke_DB.close()
