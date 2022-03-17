from flask import Flask, render_template, request
import pickle
import pandas as pd

loaded_model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def hello_world():
    return render_template("home.html")


@app.route('/', methods=["POST"])
@cross_origin()
def predict():
    # Source ----------------------------
    Source = request.form["source"]
    if Source == 'Delhi':
        Source_Delhi = 1
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0

    elif Source == 'Kolkata':
        Source_Delhi = 0
        Source_Kolkata = 1
        Source_Mumbai = 0
        Source_Chennai = 0

    elif Source == 'Mumbai':
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 1
        Source_Chennai = 0

    elif Source == 'Chennai':
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 1

    else:
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0

        # Destination -----------------------------
    destination = request.form["destination"]

    if destination == 'Cochin':
        Cochin = 1
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 0

    elif destination == 'New_Delhi':
        Cochin = 0
        New_Delhi = 1
        Hyderabad = 0
        Kolkata = 0

    elif destination == 'Hyderabad':
        Cochin = 0
        New_Delhi = 0
        Hyderabad = 1
        Kolkata = 0

    elif destination == 'Kolkata':
        Cochin = 0
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 1

    else:
        Cochin = 0
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 0

    # dateofjourney -----------------------------

    dateofjourney = request.form["dateofjourney"]

    Journey_day = int(pd.to_datetime(dateofjourney).day)
    Journey_month = int(pd.to_datetime(Journey_day).month)

    # dep_time -----------------------------

    dep_time = request.form["dep_time"]

    Dep_hour = int(pd.to_datetime(dep_time).hour)
    Dep_min = int(pd.to_datetime(dep_time).minute)

    # arr_time -----------------------------

    arr_time = request.form["arr_time"]

    Arrival_hour = int(pd.to_datetime(arr_time).hour)
    Arrival_min = int(pd.to_datetime(arr_time).minute)

    # total_stop -----------------------------

    total_stop = request.form["total_stop"]

    # airline -----------------------------

    airline = request.form["airline"]
    if airline == 'Jet Airways':
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'IndiGo':
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'Air India':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'Multiple carriers':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'SpiceJet':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'Vistara':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'GoAir':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'Multiple carriers Premium economy':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'Jet Airways Business':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif airline == 'Vistara Premium economy':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0

    elif airline == 'Trujet':
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    # Prediction-------------------------------------------------------------
    values = [
        total_stop,

        Air_India,
        IndiGo,
        GoAir,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        SpiceJet,
        Trujet,
        Vistara,
        Vistara_Premium_economy,

        Journey_day,
        Journey_month,

        Source_Chennai,
        Source_Delhi,
        Source_Kolkata,
        Source_Mumbai,

        Cochin,
        Hyderabad,
        Kolkata,
        New_Delhi,

        Dep_hour,
        Dep_min,

        Arrival_hour,
        Arrival_min,

    ]
    for i in values:
        if i is not None:
            prediction = loaded_model.predict([[
                total_stop,

                Air_India,
                IndiGo,
                GoAir,
                Jet_Airways,
                Jet_Airways_Business,
                Multiple_carriers,
                Multiple_carriers_Premium_economy,
                SpiceJet,
                Trujet,
                Vistara,
                Vistara_Premium_economy,

                Journey_day,
                Journey_month,

                Source_Chennai,
                Source_Delhi,
                Source_Kolkata,
                Source_Mumbai,

                Cochin,
                Hyderabad,
                Kolkata,
                New_Delhi,

                Dep_hour,
                Dep_min,

                Arrival_hour,
                Arrival_min,

            ]])
        else:
            prediction = "Value Error"

    output = round(prediction[0], 2)

    return render_template("home.html",
                           prediction=output)


if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  app.run(host='0.0.0.0', port=port)
