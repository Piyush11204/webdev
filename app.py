

from flask import Flask, flash,  render_template, request, url_for, redirect ,jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
client = MongoClient('localhost', 27017)
@app.route("/add", methods=('GET', 'POST'))
def add():
    if request.method == "POST":   
        content = request.form['content']
        degree = request.form['degree']
        uname =request.form['uname']
        number=request.form['number']
        vender.insert_one({'content': content, 'degree': degree, 'uname': uname,'number':number})
        return redirect(url_for('recently')) # redirect the user to home page
    all_vender = vender.find()    # display all todo documents
    return render_template('add.html', vender = all_vender) # render home page template with all vender

def add():
      return render_template( 'add.html' )

@app.route('/')
def index():
    return  render_template('index.html')
@app.route('/contact')
def contact():
    return render_template( 'contact.html' )

#for contact input
@app.route("/contact", methods=('GET', 'POST'))
def sendmail():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        contact = request.form["contact"]
        message = request.form["message"]
        
        flash("Your message is sent successfully")
        contact_collection = db.contact_collection
        contact_collection.insert_one({'name':name,'email':email,'contact':contact,'message':message})
    
        return render_template("contact.html")  
    
  
@app.route('/add',methods=['POST'])
@app.route('/contact',methods=['POST'])

 
@app.route('/home')
def landingPage():
    return render_template('index.html')

@app.route('/recently')
def recently():
     all_vender = vender.find() 
     return render_template('recently.html', vender = all_vender)
    
@app.route('/about')
def about():
    return  render_template('about.html')


@app.post("/<id>/delete/")
def delete(id): #delete function by targeting a todo document by its own id
    vender.delete_one({"_id":ObjectId(id)}) #deleting the selected todo document by its converted id
    return redirect(url_for('add')) # again, redirecting you to the home page 
db = client.StyleIT # creating your flask database using your mongo client 
vender = db.vender # creating a collection called "vender"



if __name__ == "__main__":
    app.run(debug=True, port=8000)
