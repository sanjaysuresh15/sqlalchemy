import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)



# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def index():
    print("All index listed below...")
    return ("/api/v1.0/precipitation", "/api/v1.0/stations", "/api/v1.0/tobs", "/api/v1.0/<start>", "/api/v1.0/<start>/<end>")


# #4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    que = [Measurement.date, Measurement.prcp]

# # Calculate the date 1 year ago from the last data point in the database
    dt.date(2017, 8, 23) - dt.timedelta(days=365)

# # Perform a query to retrieve the data and precipitation scores
    rain_year = session.query(*que).\
    filter(func.strftime("%Y-%m-%d", Measurement.date) >= dt.date(2017, 8, 23) - dt.timedelta(days=365)  ).\
    group_by(Measurement.date).\
    order_by(Measurement.date).all()
    
    data_list = []
  

    for data in rain_year:
         data_dictionary = {}
         data_dictionary['Date'] = data.date
         data_dictionary['Prcp'] = data.prcp
         data_list.append(data_dictionary)
       
    return jsonify(data_list)

#@app.route("/api/v1.0/stations")
##def about():
   ## print("Server received request for 'About' page...")
   # return "Welcome to my 'About' page!"



#@app.route("/api/v1.0/tobs")
#def about():
    ###print("Server received request for 'About' page...")
   # return "Welcome to my 'About' page!"


#@app.route("@app.route("/api/v1.0/<start> and /api/v1.0/<start>/<end>")
##def about():
    ##print("Server received request for 'About' page...")
   # return "Welcome to my 'About' page!"")



if __name__ == "__main__":
    app.run(debug=True)