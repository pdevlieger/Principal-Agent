from flask import Flask, render_template, request, redirect, url_for
from pridil import get_payoffs, get_all_strategies
from strategies import strategies
import numpy as np
import os

app = Flask(__name__)

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

def get_value(form_input, default):
    if request.form[form_input]:
        return int(request.form[form_input])
    else:
        return default

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<strategy_name>', methods=["GET", "POST"])
def strategy_overview(strategy_name):
    if request.method == "GET":
        dict, array, max = get_payoffs(strategies[strategy_name], 200, 3, 1, 0, 5, True, None)
        return render_template('strat_overview.html', dict=dict, array=array, redirection=strategy_name, iterations=200, max=max, name=strategies[strategy_name].__doc__)
    else:
        iterations = get_value('iterations', 200)
        coop = get_value('coop', 3)
        defect = get_value('defect', 1)
        sucker = get_value('sucker', 0)
        winner = get_value('winner', 5)
        dict, array, max = get_payoffs(strategies[strategy_name], iterations, coop, defect, sucker, winner, True, None)
        return render_template('strat_overview.html', dict=dict, array=array, redirection=strategy_name, iterations=iterations, max=max, name=strategies[strategy_name].__doc__)

@app.route('/overview', methods=["GET", "POST"])
def overview():
    if request.method == "GET":
        dict, max = get_all_strategies(200, 3, 1, 0, 5, None)
        averages = {k: v[-1]/len(v) for k,v in dict.iteritems()}
        return render_template('overview.html', dict=dict, iterations=200, max=max, averages=averages)
    else:
        weights={}
        iterations = get_value('iterations', 200)
        coop = get_value('coop', 3)
        defect = get_value('defect', 1)
        sucker = get_value('sucker', 0)
        winner = get_value('winner', 5)
        weights['ac'] = get_value('ac', 1)
        weights['ad'] = get_value('ad', 1)
        weights['c_70'] = get_value('c_70', 1)
        weights['c_switch'] = get_value('c_switch', 1)
        weights['c_until_d'] = get_value('c_until_d', 1)
        weights['d_70'] = get_value('d_70', 1)
        weights['d_switch'] = get_value('d_switch', 1)
        weights['ntft'] = get_value('ntft', 1)
        weights['rand'] = get_value('rand', 1)
        weights['tft'] = get_value('tft', 1)
        dict, max = get_all_strategies(iterations, coop, defect, sucker, winner, weights)
        average_population = sum([v for v in weights.values()])/len(weights)
        averages = {k: v[-1]/(iterations*average_population) for k,v in dict.iteritems()}
        return render_template('overview.html', dict=dict, iterations=iterations, max=max, averages=averages)


if __name__ == '__main__':
    port_number = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port_number, debug=True)
