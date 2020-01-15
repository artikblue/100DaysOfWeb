from program import app
from flask import render_template, request

from datetime import datetime

import requests


@app.route('/')
@app.route('/index')
def index():
    timenow = str(datetime.today())
    return render_template("index.html", time=timenow)

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/chuck')
def chuck_api():
    chuck_api_url = "https://api.chucknorris.io/jokes/random"
    new_joke = requests.get(chuck_api_url)

    return render_template("chuck.html", joke=new_joke.json())

@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
    pokemon = []
    if request.method =='POST' and 'pokecolour' in request.form:
        
        colour = request.form.get('pokecolour')
        pokemon = get_poke_colours(colour)

    return render_template('pokemon.html', pokemon = pokemon)

def get_all_colours():
    colours = []
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/')
    coloursdata = r.json()

    for c in coloursdata["results"]:
        colours.append(c["name"])
    return colours

def get_poke_colours(colour):
    pokemon = []
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + colour.lower())
    try:
        pokedata = r.json()
    except Exception as e:
        print(e)
        pokedata = []

    if pokedata:
        for i in pokedata['pokemon_species']:
            pokemon_name = i["name"]
            pokeinfo = get_poke_info(pokemon_name)

            if pokeinfo:
                pokeobject = {
                    "name":pokemon_name,
                    "order": pokeinfo["order"],
                    "weight": pokeinfo["weight"],
                    "height": pokeinfo["height"],
                    "types": pokeinfo["types"],
                    "area": pokeinfo["location_area_encounters"]
                }
                pokemon.append(pokeobject)
    return pokemon

def get_poke_info(pokename):
    pokeinfo = {}
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokename)
    try:
        pokeinfo = r.json()
    except Exception as e:
        print(e)
    return pokeinfo