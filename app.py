from flask import Flask, render_template, request, redirect, flash, url_for
import pymysql

app = Flask(__name__)
app.secret_key = "petshopcdl_secret"

# Configurações do banco de dados
db = pymysql.connect(
    host="localhost",
    user="root",
    password="0703LT2023.",
    database="petshopcdl"
)

# Rota inicial
@app.route("/")
def index():
    return render_template("index.html")

# CRUD para Pets
@app.route("/pets")
def list_pets():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()
    cursor.close()
    return render_template("pets.html", pets=pets)

@app.route("/pets/add", methods=["GET", "POST"])
def add_pet():
    if request.method == "POST":
        name = request.form["name"]
        species = request.form["species"]
        age = request.form["age"]
        tutor_id = request.form["tutor_id"]
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO pets (name, species, age, tutor_id) VALUES (%s, %s, %s, %s)",
            (name, species, age, tutor_id)
        )
        db.commit()
        cursor.close()
        flash("Pet added successfully!")
        return redirect(url_for("list_pets"))
    return render_template("add_edit_pet.html", pet=None)

@app.route("/pets/edit/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pets WHERE id = %s", (id,))
    pet = cursor.fetchone()
    cursor.close()
    if request.method == "POST":
        name = request.form["name"]
        species = request.form["species"]
        age = request.form["age"]
        tutor_id = request.form["tutor_id"]
        cursor = db.cursor()
        cursor.execute(
            "UPDATE pets SET name=%s, species=%s, age=%s, tutor_id=%s WHERE id=%s",
            (name, species, age, tutor_id, id)
        )
        db.commit()
        cursor.close()
        flash("Pet updated successfully!")
        return redirect(url_for("list_pets"))
    return render_template("add_edit_pet.html", pet=pet)

@app.route("/pets/delete/<int:id>")
def delete_pet(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM pets WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    flash("Pet deleted successfully!")
    return redirect(url_for("list_pets"))

# CRUD para Tutors
@app.route("/tutors")
def list_tutors():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tutors")
    tutors = cursor.fetchall()
    cursor.close()
    return render_template("tutors.html", tutors=tutors)

@app.route("/tutors/add", methods=["GET", "POST"])
def add_tutor():
    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["contact"]
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO tutors (name, contact) VALUES (%s, %s)",
            (name, contact)
        )
        db.commit()
        cursor.close()
        flash("Tutor added successfully!")
        return redirect(url_for("list_tutors"))
    return render_template("add_edit_tutor.html", tutor=None)

@app.route("/tutors/edit/<int:id>", methods=["GET", "POST"])
def edit_tutor(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tutors WHERE id = %s", (id,))
    tutor = cursor.fetchone()
    cursor.close()
    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["contact"]
        cursor = db.cursor()
        cursor.execute(
            "UPDATE tutors SET name=%s, contact=%s WHERE id=%s",
            (name, contact, id)
        )
        db.commit()
        cursor.close()
        flash("Tutor updated successfully!")
        return redirect(url_for("list_tutors"))
    return render_template("add_edit_tutor.html", tutor=tutor)

@app.route("/tutors/delete/<int:id>")
def delete_tutor(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tutors WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    flash("Tutor deleted successfully!")
    return redirect(url_for("list_tutors"))

# CRUD para Consultations
@app.route("/consultations")
def list_consultations():
    cursor = db.cursor()
    cursor.execute("""
        SELECT consultations.id, pets.name, consultations.date, consultations.description 
        FROM consultations
        JOIN pets ON consultations.pet_id = pets.id
    """)
    consultations = cursor.fetchall()
    cursor.close()
    return render_template("consultations.html", consultations=consultations)

@app.route("/consultations/add", methods=["GET", "POST"])
def add_consultation():
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM pets")
    pets = cursor.fetchall()
    cursor.close()
    if request.method == "POST":
        pet_id = request.form["pet_id"]
        date = request.form["date"]
        description = request.form["description"]
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO consultations (pet_id, date, description) VALUES (%s, %s, %s)",
            (pet_id, date, description)
        )
        db.commit()
        cursor.close()
        flash("Consultation added successfully!")
        return redirect(url_for("list_consultations"))
    return render_template("add_edit_consultation.html", consultation=None, pets=pets)

@app.route("/consultations/edit/<int:id>", methods=["GET", "POST"])
def edit_consultation(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM consultations WHERE id = %s", (id,))
    consultation = cursor.fetchone()
    cursor.execute("SELECT id, name FROM pets")
    pets = cursor.fetchall()
    cursor.close()
    if request.method == "POST":
        pet_id = request.form["pet_id"]
        date = request.form["date"]
        description = request.form["description"]
        cursor = db.cursor()
        cursor.execute(
            "UPDATE consultations SET pet_id=%s, date=%s, description=%s WHERE id=%s",
            (pet_id, date, description, id)
        )
        db.commit()
        cursor.close()
        flash("Consultation updated successfully!")
        return redirect(url_for("list_consultations"))
    return render_template("add_edit_consultation.html", consultation=consultation, pets=pets)

@app.route("/consultations/delete/<int:id>")
def delete_consultation(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM consultations WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    flash("Consultation deleted successfully!")
    return redirect(url_for("list_consultations"))

if __name__ == "__main__":
    app.run(debug=True)
