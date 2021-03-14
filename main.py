from flask import Flask, Response, request, render_template
import lib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('design.html')


@app.route('/', methods=["POST","GET"])
def respond():
    location = request.form['location']
    coordinates = lib.to_coords(location)
    print(coordinates)
    print("Latitude = {}, Longitude = {}".format(coordinates.longitude, coordinates.latitude))
    return nearest_name("addresses.txt", location)

if __name__ == "__main__":
    app.run()
