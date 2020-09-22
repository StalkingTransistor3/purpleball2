from flask import Flask, render_template, session, request
import requests
from bs4 import BeautifulSoup



import pandas as pd
import numpy as np
import pandasql as ps
import unicodedata

app = Flask(__name__)

app.secret_key = 's3cr3t'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/HomeMk4')
def HomeMk4():
  # See if x is in the session
    x = session.get('x', None)
    if not x:
    # If it's not there, set it to 1
        session['x'] = 1
        print(str(session['x']))
        print("Cue Tutorial")
        tutorial = 1

    elif x>=2:
    # If it's 10, clear and start over
        session.clear()
        print("Session Cleared")
        tutorial = 0
    else:
        # If it's there, add 1
        session['x']+=1
        # Display current count
        print(str(session['x']))
        tutorial = 0
    return render_template('HomeMk4.html',
    cue_tutorial = str(tutorial)
    
    )

@app.route('/Homepage')
def Homepage3():
    return render_template('Homepage.html')

@app.route('/Help')
def Helpage():
    return render_template('helppage.html')



@app.route('/suggestions')
def suggestions():
    text = request.args.get('jsdata')

    suggestions_list = []
    print(text)
    print(suggestions_list)

    if text:
        r = requests.get('http://suggestqueries.google.com/complete/search?output=toolbar&hl=ru&q={}&gl=in'.format(text))

        soup = BeautifulSoup(r.content, 'lxml')

        suggestions = soup.find_all('suggestion')
        print(r)
        print(soup)

        for suggestion in suggestions:
            suggestions_list.append(suggestion.attrs['data'])

        #print(suggestions_list)

    return render_template('suggestions.html', suggestions=suggestions_list)

@app.route('/crime_interface')
def Crimeterface():

    df = pd.read_csv('CrimebaseMk2.csv')
    council = request.args.get('jsdata')
    print(request.args.get('jsdata'))
    records = list(df[council])

    Total_BE	= records[	0	]
    Rate_BE	= records[	1	]
    Rank_BE	= records[	2	]
    Total_DwellThef	= records[	3	]
    Rate_DwellThef	= records[	4	]
    Rank_DwellThef	= records[	5	]
    Total_MVThef	= records[	6	]
    Rate_MVThef	= records[	7	]
    Rank_MVThef	= records[	8	]
    Total_NDomVio	= records[	9	]
    Rate_NDomVio	= records[	10	]
    Rank_NDomVio	= records[	11	]
    Total_PossUsCnnbs	= records[	12	]
    Rate_PossUsCnnbs	= records[	13	]
    Rank_PossUsCnnbs	= records[	14	]
    Total_PropDmg	= records[	15	]
    Rate_PropDmg	= records[	16	]
    Rank_PropDmg	= records[	17	]
    Total_Robb	= records[	18	]
    Rate_Robb	= records[	19	]
    Rank_Robb	= records[	20	]
    Total_TeaOff	= records[	21	]
    Rate_TeaOff	= records[	22	]
    Rank_TeaOff	= records[	23	]
    Total_StelYoCar	= records[	24	]
    Rate_StelYoCar	= records[	25	]
    Rank_StelYoCar	= records[	26	]
    Total_Tress	= records[	27	]
    Rate_Tress	= records[	28	]
    Rank_Tress	= records[	29	]

    
    Total_Rank = (int(Rank_BE)+int(Rank_DwellThef)+int(Rank_MVThef)+int(Rank_NDomVio)+int(Rank_PossUsCnnbs)+int(Rank_PropDmg)+int(Rank_Robb)+int(Rank_StelYoCar)+int(Rank_TeaOff)+int(Rank_Tress))/10
    print(Total_Rank)
    
    
    

    

    return render_template('Crimepage.html',
    council = council,
    TotalRank = Total_Rank,
    BET = Total_BE,
    BERP = Rate_BE,
    BER = Rank_BE,
    DTT = Total_DwellThef,
    DTRP = Rate_DwellThef,
    DTR = Rank_DwellThef,
    MTT = Total_MVThef,
    MTRP = Rate_MVThef,
    MTR = Rank_MVThef,
    VT = Total_NDomVio,
    VRP = Rate_NDomVio,
    VR = Rank_NDomVio,
    PUCT = Total_PossUsCnnbs,
    PUCRP = Rate_PossUsCnnbs,
    PUCR = Rank_PossUsCnnbs,
    PDT = Total_PropDmg,
    PDRP = Rate_PropDmg,
    PDR = Rank_PropDmg,
    RBT = Total_Robb,
    RBRP = Rate_Robb,
    RBR = Rank_Robb,
    SOT = Total_TeaOff,
    SORP = Rate_TeaOff,
    SOR = Rank_TeaOff,
    TMT = Total_StelYoCar,
    TMRP = Rate_StelYoCar,
    TMR = Rank_StelYoCar,
    TT = Total_Tress,
    TRP = Rate_Tress,
    TR = Rank_Tress

    
    )


@app.route('/infrastructure')
def infrastructure():
    df = pd.read_csv('CoordsSelected.csv')
    sub = request.args.get('jsdata')
    print(request.args.get('jsdata'))
    subCAPS = sub.upper()
    print(subCAPS)
    records = list(df[subCAPS])

    postcode = int(records[0])
    distcbd = int(records[5])

    return render_template("infrastructure.html", postcode = postcode, distcbd = distcbd)

@app.route('/crimeranksorter')
def crimeranksorter():
    df = pd.read_csv('CrimebaseMk2.csv')
    df_inverted = pd.read_csv('CrimebaseMk2INVERTED.csv')
    council = request.args.get('jsdata')
    print(request.args.get('jsdata'))
    records = list(df[council])

    
    Rank_BE	= records[	2	]
    Rank_DwellThef	= records[	5	]
    Rank_MVThef	= records[	8	]
    Rank_NDomVio	= records[	11	]
    Rank_PossUsCnnbs	= records[	14	]
    Rank_PropDmg	= records[	17	]
    Rank_Robb	= records[	20	]
    Rank_TeaOff	= records[	23	]
    Rank_StelYoCar	= records[	26	]
    Rank_Tress	= records[	29	]

    
    Total_Rank = (int(Rank_BE)+int(Rank_DwellThef)+int(Rank_MVThef)+int(Rank_NDomVio)+int(Rank_PossUsCnnbs)+int(Rank_PropDmg)+int(Rank_Robb)+int(Rank_StelYoCar)+int(Rank_TeaOff)+int(Rank_Tress))/10
    print(Total_Rank)
    
    
    


    

    return render_template("ranks.html", rank = Total_Rank)

@app.route('/ranksearch')
def ranksearch():
    df = pd.read_csv('CrimebaseMk2.csv')
    df_inverted = pd.read_csv('CrimebaseMk2INVERTED.csv')
    crime = request.args.get('jsdata')
    print(request.args.get('jsdata'))

    Leaderboard = df_inverted.nlargest(32, crime)
    print(Leaderboard)
    Leaderboard_records = list(Leaderboard["LGA"])
    print(Leaderboard_records)

    return render_template("ranksearch.html",

        crime = crime,
        
        rank1 = Leaderboard_records[0], 
        rank2 = Leaderboard_records[1],
        rank3 = Leaderboard_records[2],
        rank4 = Leaderboard_records[3],
        rank5 = Leaderboard_records[4],
        rank6 = Leaderboard_records[5],
        rank7 = Leaderboard_records[6],
        rank8 = Leaderboard_records[7],
        rank9 = Leaderboard_records[8],
        rank10 = Leaderboard_records[9],
        bottom1 = Leaderboard_records[-1],
        bottom2 = Leaderboard_records[-2],
        bottom3 = Leaderboard_records[-3],
        bottom4 = Leaderboard_records[-4],
        bottom5 = Leaderboard_records[-5],
        bottom6 = Leaderboard_records[-6],
        bottom7 = Leaderboard_records[-7],
        bottom8 = Leaderboard_records[-8],
        bottom9 = Leaderboard_records[-9],
        bottom10 = Leaderboard_records[-10],

        )


@app.route('/price_predictor')
def price_predictor():

    df = pd.read_csv('PredictionsINVERTED.csv')
    df2 = pd.read_csv('suburb_dataINVERTED.csv')
    suburb = request.args.get('jsdata')
    print(request.args.get('jsdata'))
    records = list(df[suburb])
    data = list(df2[suburb])
    print(records)
    print(records[-1])
    threshold = int(records[-1])
    gini = records[-2]
    if threshold == 0:
        prediction = "The price of houses in this suburb will fall"
        confidence = int(100*-((10/3)*gini-1))
    else:
        prediction = "The price of houses in this suburb will rise"
        confidence =int(100*((10/7)*gini-(3/7)))


    

    return render_template("price_predictor.html",
    suburb = suburb,
    prediction = prediction,
    confidence = confidence,
    messenger = threshold,
    min = data[2],
    max = data[6],
    mean = data[14],
    std = data[10],
    median = data[18]


    )

@app.route('/suburbs_by_council')
def suburbs_by_council():
    df = pd.read_csv("subbycoun.csv")
    council = request.args.get('jsdata')
    suburbs = list(df[council].dropna())

    
    print(suburbs)


    return render_template("suburbsbycouncil.html",
    suburbs = suburbs
    )






if __name__ == '__main__':
    
  app.run(host='0.0.0.0', debug=True)
