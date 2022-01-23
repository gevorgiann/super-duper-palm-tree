from distutils.command.build import build
from operator import truediv
from flask import Flask
from flask import render_template
from flask import redirect, url_for, request
import statistics


app = Flask(__name__)
db = []
class Building:
    def __init__ (self):
        self.floors = 1
        self.ada_comp = False
        self.building_name = ""
        self.building_rating = []
        self.building_review = []
        self.average_rating = 0
#(optional) error handle for zero items on the average rating

# tuple for (rating, review)
# when displaying tuple above, sort rating from best to worst and present some of the best and some of the worst 
# optional - add button to view all reviews 
# hard code a lot of ratings into array

building1 = Building()
building1.floors = 2
building1.ada_comp = True
building1.building_name = "Sol Center"
building1.building_rating = [5, 5, 4, 1, 2, 5, 3, 1, 4]
building1.building_review = ['This place was amazing!', 'this place sucks', 'this place was alirght', 'Too much sol']
building1.average_rating = statistics.mean(building1.building_rating)

building2 = Building()
building2.floors = 1
building2.ada_comp = True
building2.building_name = "Oasis"
building2.building_rating = [ 5, 1, 4, 1,3, 1,4,5,5,2,4,2, 5, 3, 1, 4]
building2.building_review = ['This place was amazing!', 'Always so clean', 'Stinks in there', 'So peaceful here']
building2.average_rating = statistics.mean(building2.building_rating)


building3 = Building()
building3.floors = 3
building3.ada_comp = True
building3.building_name = "SRC"
building3.building_rating = [5, 5, 4, 1,3,4,5,2,1,3,3, 2, 5, 3, 1, 4]
building3.building_review = ['Dope spot!', 'Perfect place to get shredded', 'Was nice Pre-Covid, not anymore', 'this place is pushing P']
building3.average_rating = statistics.mean(building3.building_rating)


db.append(building1)
db.append(building2)
db.append(building3)

@app.route("/buildings")
def buildings():
    building_info = ""
    for building in db:
        building_info += f"<p>{building.building_name}</p>"

    return render_template('buildings.html', buildings = db)

# @app.route("/ratings")
# def ratings():
#     building_info = ""
#     for building in db:
#         building_info += f"<p>{building.building_rating}</p>"

#     return render_template('ratings.html', buildings = db)

@app.route('/ratings', methods =["GET", "POST"])
def rating():
    building_info = ""
    if request.method == "POST":
       # getting input in HTML form
       building_rating = int(request.form.get("building_rating"))
       building_review = request.form.get("building_review")
       building_name = request.form.get("building_name")

       for building in db:
           if building.building_name == building_name:
                building.building_rating.append(building_rating)
                building.building_review.append(building_review)
                building.average_rating = statistics.mean(building.building_rating)
                return redirect(url_for("view"))

      # return  '{} {}'.format(building_rating) possible tuple format for rating and review
    return render_template('ratings.html', buildings = db)


@app.route("/view")
def view():
    building_info = ""
    for building in db:
        building_info += f"<p>{building.building_rating}</p>"
                
    return render_template('view.html', buildings = db)


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
    return redirect(url_for('jade'))
