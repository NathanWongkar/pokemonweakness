from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokemon', methods=['POST'])
def pokemon():
    pokemon_name = request.form['name']
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/").json()

    types = response["types"]
    immunities = []
    resistances = []
    weaknesses = []

    for type_data in types:
        type_url = type_data["type"]["url"]
        type_response = requests.get(type_url).json()
        damage_relations = type_response["damage_relations"]
        for array_name, type_list in [("no_damage_from", immunities), ("half_damage_from", resistances), ("double_damage_from", weaknesses)]:
            for weak_type in damage_relations[array_name]:
                weak_type_response = requests.get(weak_type["url"]).json()
                type_list.append(weak_type_response["name"])

    return render_template('pokemon.html', name=pokemon_name, types=types, immunities=immunities, resistances=resistances, weaknesses=weaknesses)

if __name__ == '__main__':
    app.run(port=5500)
