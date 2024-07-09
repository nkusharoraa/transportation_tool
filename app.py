from flask import Flask, render_template, request
from models import db, TransportMode
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modes.db'
db.init_app(app)

initialized = False

def create_tables():
    db.create_all()
    load_initial_data()

def load_initial_data():
    if TransportMode.query.count() == 0:
        data = pd.read_csv('transport_modes.csv')
        for _, row in data.iterrows():
            mode = TransportMode(mode=row['mode'],
                                 cost_per_mile=row['cost_per_mile'],
                                 time_per_mile=row['time_per_mile'],
                                 emissions_per_mile=row['emissions_per_mile'])
            db.session.add(mode)
        db.session.commit()

@app.before_request
def initialize():
    global initialized
    if not initialized:
        create_tables()
        initialized = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    distance = float(request.form['distance'])
    weight = float(request.form['weight'])
    
    modes = TransportMode.query.all()
    recommendations = []
    
    for mode in modes:
        total_cost = distance * mode.cost_per_mile * weight
        total_time = distance * mode.time_per_mile
        total_emissions = distance * mode.emissions_per_mile * weight
        
        recommendations.append({
            'mode': mode.mode,
            'total_cost': total_cost,
            'total_time': total_time,
            'total_emissions': total_emissions
        })
    
    recommendations.sort(key=lambda x: (x['total_cost'], x['total_time'], x['total_emissions']))
    
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
