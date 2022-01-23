from distutils.command.build import build
from genericpath import exists
from operator import truediv
from flask import Flask
from flask import render_template
from flask import redirect, url_for, request, redirect, abort, send_from_directory
import statistics
from werkzeug.utils import secure_filename
import imghdr
import os



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

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'upload'
if not os.path.exists('upload'):  
    os.mkdir('upload')

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/upload')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('upload.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return '', 204

@app.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route("/")
def bottom():
    return redirect(url_for('jade'))
