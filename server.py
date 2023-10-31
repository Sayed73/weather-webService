from flask import Flask ,render_template,request
from weatherApp import get_curr_weather

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        return render_template('city-not-found.html')

    weather_data = get_curr_weather(city)

    # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')


    return render_template(
        'weather.html',
        title= weather_data["name"],
        country = weather_data["sys"]["country"],
        status=weather_data['weather'][0]['description'].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        lat_coord = weather_data["coord"]["lat"],
        long_coord = weather_data["coord"]["lon"],   
    )


if __name__ == '__main__':
    app.run(debug=True,port=5050)