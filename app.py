from operator import truediv
from flask import Flask
from flask import render_template
from flask import redirect, url_for



app = Flask(__name__)
db = []
class Building:
    def __init__ (self):
        self.floors = 1
        self.ada_comp = False
        self.building_name = ""
building1 = Building()
building1.floors = 4
building1.ada_comp = True
building1.building_name = "jacaranda"
db.append(building1)

@app.route("/buildings")
def buildings():
    building_info = ""
    for building in db:
        building_info += f"<p>{building.building_name}</p>"

    return render_template('buildings.html', buildings = db)

@app.route("/buildings/<building_name>")
def building(building_name):
    building_info = ""
    for building in db:
        if building.building_name == building_name:
            return render_template('building.html', building = building)
    return redirect(url_for('buildings'))


@app.route("/")
def hello_world():
    return render_template('base.html')
