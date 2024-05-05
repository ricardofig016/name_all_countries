import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from icecream import ic


FILE_NAME = "countries.json"
with open(FILE_NAME, "r") as file:
    COUNTRY_DATA = json.load(file)
OPTIONS = {
    "include territories": False,
}


app = Flask(__name__)


@app.route("/")
def index():
    country_names = get_display_country_names()
    col_amount = len(country_names) // 23 + 1
    return render_template(
        "index.html",
        country_names=country_names,
        col_amount=col_amount,
        col_size=len(country_names) // col_amount + 1,
    )


@app.route("/process_input", methods=["POST"])
def process_input():
    input = request.json.get("input_value")
    formated_input = format_country_name(input)
    for country in COUNTRY_DATA:
        if (
            country["state"] == "not guessed"
            and country["formated name"] in formated_input
        ):
            country["state"] = "guessed"
            return jsonify({"modified": True, "countries": get_display_country_names()})

    return jsonify({"modified": False})


def get_display_country_names():
    country_names = []
    filtered_data = COUNTRY_DATA
    if not OPTIONS["include territories"]:
        filtered_data = [
            country
            for country in COUNTRY_DATA
            if country["category"] != "Other Territories"
        ]
    for country in filtered_data:
        if country["state"] == "not guessed":
            country_names.append("-" * len(country["name"]))
        elif country["state"] == "guessed":
            country_names.append(country["name"])
    ic(len(country_names))
    return country_names


def format_country_name(name):
    return "".join(ch for ch in name.lower() if ch not in [" ", "-"])


if __name__ == "__main__":
    app.run(debug=True)
