import sqlite3

# Connect to the database
conn = sqlite3.connect('valgykla.db')
cursor = conn.cursor()

# Create table for Employees
cursor.execute('''CREATE TABLE IF NOT EXISTS Darbuotojai
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                vardas TEXT NOT NULL,
                pareigos TEXT NOT NULL)''')

# Create table for Menu
cursor.execute('''CREATE TABLE IF NOT EXISTS Meniu
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                pavadinimas TEXT NOT NULL,
                kaina REAL NOT NULL)''')


def sukurti_darbuotoja():
    vardas = input("Įveskite darbuotojo vardą: ")
    pareigos = input("Įveskite darbuotojo pareigas: ")
    cursor.execute("INSERT INTO Darbuotojai (vardas, pareigos) VALUES (?, ?)", (vardas, pareigos))
    conn.commit()
    print("Darbuotojas sukurtas sėkmingai!")


def skaityti_darbuotojus():
    cursor.execute("SELECT * FROM Darbuotojai")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Darbuotojų nerasta.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Vardas: {row[1]}, Pareigos: {row[2]}")


def redaguoti_darbuotoja():
    darbuotojo_id = input("Įveskite darbuotojo ID, kurį norite redaguoti: ")
    cursor.execute("SELECT * FROM Darbuotojai WHERE id = ?", (darbuotojo_id,))
    row = cursor.fetchone()
    if row is None:
        print("Darbuotojas su nurodytu ID nerastas.")
    else:
        vardas = input("Įveskite naują vardą: ")
        pareigos = input("Įveskite naujas pareigas: ")
        cursor.execute("UPDATE Darbuotojai SET vardas = ?, pareigos = ? WHERE id = ?", (vardas, pareigos, darbuotojo_id))
        conn.commit()
        print("Darbuotojas atnaujintas sėkmingai!")


def prideti_i_meni():
    pavadinimas = input("Įveskite patiekalo pavadinimą: ")
    kaina = float(input("Įveskite patiekalo kainą: "))
    cursor.execute("INSERT INTO Meniu (pavadinimas, kaina) VALUES (?, ?)", (pavadinimas, kaina))
    conn.commit()
    print("Patiekalas pridėtas į meniu sėkmingai!")


def rodyti_meni():
    cursor.execute("SELECT * FROM Meniu")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Meniu elementų nerasta.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Pavadinimas: {row[1]}, Kaina: {row[2]}")


def pagrindinis_meniu():
    while True:
        print("\n--- Valgyklos Valdymo Sistema ---")
        print("1. Sukurti Darbuotoją")
        print("2. Skaityti Darbuotojus")
        print("3. Redaguoti Darbuotoją")
        print("4. Pridėti patiekalą į Meniu")
        print("5. Rodyti Meniu")
        print("0. Išeiti")
        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == "1":
            sukurti_darbuotoja()
        elif pasirinkimas == "2":
            skaityti_darbuotojus()
        elif pasirinkimas == "3":
            redaguoti_darbuotoja()
        elif pasirinkimas == "4":
            prideti_i_meni()
        elif pasirinkimas == "5":
            rodyti_meni()
        elif pasirinkimas == "0":
            break
        else:
            print("Netinkamas pasirinkimas. Bandykite dar kartą.")


# Run the main menu
pagrindinis_meniu()

# Close the database connection
conn.close()
