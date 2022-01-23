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
        self.building_rating = [] 
# error handle for zero items on the average rating
#make calc avergae function

# tuple for (rating, review)
# when displaying tuple above, sort rating from best to worst and present some of the best and some of the worst 
# add button to view all reviews 
# hard code a lot of ratings into array

building1 = Building()
building1.floors = 2
building1.ada_comp = True
building1.building_name = "Sol Center"
building1.building_rating 

building2 = Building()
building2.floors = 1
building2.ada_comp = True
building2.building_name = "Oasis"
building2.building_rating 

building3 = Building()
building3.floors = 3
building3.ada_comp = True
building3.building_name = "SRC"
building3.building_rating 

db.append(building1)
db.append(building2)
db.append(building3)

@app.route("/buildings")
def buildings():
    building_info = ""
    for building in db:
        building_info += f"<p>{building.building_name}</p>"

    return render_template('buildings.html', buildings = db)

@app.route("/ratings")
def ratings():
    building_info = ""
    for building in db:
        building_info += f"<p>{building.building_rating}</p>"

    return render_template('ratings.html', buildings = db)

@app.route("/buildings/<building_name>")
def building(building_name):
    building_info = ""
    for building in db:
        if building.building_name == building_name:
            return render_template('building.html', building = building)
    return redirect(url_for('buildings'))
    
@app.route("/index")
def jade():
    building_info = ""
    return render_template('index.html')

@app.route("/")
def bottom():
    return render_template('base.html')
