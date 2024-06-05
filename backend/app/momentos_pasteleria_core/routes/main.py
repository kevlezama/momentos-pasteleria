from flask import Blueprint, jsonify


main_bp = Blueprint('main', __name__)

@main_bp.route('/',methods=['GET'])
@main_bp.route('/home', methods=['GET'])
def home():
    test = {

        'DNI': 95851445,
        'name':'kevin',
        'last_name':'lezama',
        'user_tier':'Tier 1'
    }

    return jsonify(test)

