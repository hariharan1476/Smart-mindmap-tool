from flask import Blueprint, render_template, request, jsonify
from .nlp_model import suggest_related_ideas

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/suggest', methods=['POST'])
def suggest():
    user_input = request.form['user_input']
    suggestions = suggest_related_ideas(user_input)
    return jsonify(suggestions=suggestions)
