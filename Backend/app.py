from flask import Flask, render_template, request
from pymeteosource.types import sections, langs, units
from pathlib import Path
import json
import os
from pymeteosource.api import Meteosource
from pymeteosource.types import tiers


YOUR_API_KEY = 'bgo7a3ste7iwx2k8et4wyd84d254or0kdl60ynl6'

YOUR_TIER = tiers.FREE

meteosource = Meteosource(YOUR_API_KEY, YOUR_TIER)

dataset = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../Dataset/data.json")
base_path = Path(__file__).parent
homepage_html = (base_path / "../Frontend/homepage.html").resolve()

app = Flask(__name__, template_folder='../Frontend', static_folder='../Frontend')

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/findtrip", methods=['GET', 'POST'])
def findtrip():
    if request.method == 'POST':
        adventure_pr = int(request.form['adventure_priority'])
        safety_pr = int(request.form['safety_priority'])
        weather_pr = int(request.form['weather_priority'])
        luxury_pr = int(request.form['luxury_priority'])
        print(adventure_pr, safety_pr, weather_pr, luxury_pr)

        score_dict={}
        with open(dataset, "r", encoding="utf-8") as f:
            data = json.load(f)
            for d in data:
                adv_score=d["adventure_rating"]*adventure_pr
                safe_score=d["safety_rating"]*safety_pr
                weather_score=d["weather_rating"]*weather_pr
                luxury_score=d["luxury_rating"]*luxury_pr
                score=adv_score+safe_score+weather_score+luxury_score
                name=d["place"]
                score_dict[name]=score

        data=max(score_dict, key=score_dict.get)
        print(data)
        return render_template('findtrip.html', data=data)
    return render_template('findtrip.html', data=None)

@app.route("/forecast/<name>")
def forecast(name=None):
    forecast_res = meteosource.get_point_forecast(
        place_id=name,  
        sections=[sections.CURRENT, sections.HOURLY],
        tz='US/Pacific',  
        lang=langs.ENGLISH, 
        units=units.US  
    )
    print(round((forecast_res.current.temperature-32)/1.8))
    return "HI"