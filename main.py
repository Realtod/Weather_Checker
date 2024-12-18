import flask
import requests
from flask import Flask, jsonify, request, render_template, make_response

app = flask.Flask(__name__)


API_KEY = '2DaApDiYAFptNo67JRMtEVemhiGGLlTK'
BASE_URL = 'http://dataservice.accuweather.com/'

def get_weather(latitude, longitude):
    location_url = f"{BASE_URL}locations/v1/cities/geoposition/search"
    params = {
        "apikey": API_KEY,
        "q": f"{latitude},{longitude}"
    }
    response = requests.get(location_url, params=params)
    # response = requests.get('http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=2DaApDiYAFptNo67JRMtEVemhiGGLlTK&q=55.7558,37.6173')
    response.raise_for_status()
    location_data = response.json()
    location_key = location_data["Key"]

    # Получить погоду по LocationKey
    weather_url = f"{BASE_URL}forecasts/v1/hourly/1hour/{location_key}"
    params = {"apikey": API_KEY, "details": True}
    response = requests.get(weather_url, params=params)
    response.raise_for_status()
    weather_data = response.json()[0]

    return weather_data

# weather_data = get_weather(55.7558, 37.6173)
# print(weather_data)
#
# temperature = weather_data["Temperature"]["Value"]
# humidity = weather_data["RelativeHumidity"]
# wind_speed = weather_data["Wind"]["Speed"]["Value"] * 1.609
# rain = weather_data["RainProbability"]
#
# print(temperature, humidity, wind_speed, rain)


def check_bad_weather(temperature, humidity, wind_speed, rain):
    if temperature < -10 or temperature > 35:
        return True
    elif wind_speed > 45:
        return True
    elif humidity > 70:
        return True
    elif rain > 70:
        return True
    else:
        return False
# print(check_bad_weather(-100, humidity, wind_speed, rain))
# print(temperature, 80, wind_speed, rain)
# print(temperature, humidity, 80, rain)
# print(temperature, humidity, wind_speed, 80)




@app.route('/')
def home():
    return "Flask работает!!!!!!!!!!!!"

@app.route('/check_bad_weather', methods=['GET', 'POST'])
def check_weather():
    if request.method == 'GET':
        return render_template('get_route_points.html')
    elif request.method == 'POST':
        coordinates_beginning = request.form.get('beginning').split(',')
        weather_data_beginning = get_weather(coordinates_beginning[0], coordinates_beginning[1])
        temperature_beginning = weather_data_beginning["Temperature"]["Value"]
        humidity_beginning = weather_data_beginning["RelativeHumidity"]
        wind_speed_beginning = weather_data_beginning["Wind"]["Speed"]["Value"] * 1.609
        rain_beginning = weather_data_beginning["RainProbability"]
        weather_beginning = check_bad_weather(temperature_beginning, humidity_beginning, wind_speed_beginning, rain_beginning)

        coordinates_ending = request.form.get('ending').split(',')
        weather_data_ending = get_weather(coordinates_ending[0], coordinates_ending[1])
        temperature_ending = weather_data_ending["Temperature"]["Value"]
        humidity_ending = weather_data_ending["RelativeHumidity"]
        wind_speed_ending = weather_data_ending["Wind"]["Speed"]["Value"] * 1.609
        rain_ending = weather_data_ending["RainProbability"]
        weather_ending = check_bad_weather(temperature_ending, humidity_ending, wind_speed_ending, rain_ending)

        if request.form.get('beginning') == None:
            return "Поле 'beginning' должно быть заполнено"
        if request.form.get('ending') == None:
            return "Поле 'ending' должно быть заполнено"

        return f"Bad weather in 1-st city: {weather_beginning}, \n Bad weather in 2-nd city: {weather_ending}"

if __name__ == '__main__':
    app.run(debug=True)
