from flask import Blueprint, render_template
import json

pets = json.load(open('pets.json'))
# print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")


@bp.route('/')
def index():
    return render_template('index.html', pets=pets)


@bp.route('/new')
def new():
    return render_template('new_fact.html', pets=pets)


@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('single_pet.html', pet=pet)
