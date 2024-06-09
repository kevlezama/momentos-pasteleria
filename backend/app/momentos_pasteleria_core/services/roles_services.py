# Flask framework
from flask import Blueprint, request, jsonify

# Sqlalchemy ORM API
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

# Global config dependencies
from app.dbconfig import db
from app.momentos_pasteleria_core.models.roles_model import RolesModel

# Python buildin
import uuid
import datetime
import json
import logging

roles_bp  = Blueprint('roles', __name__)


@roles_bp.route('/roles/v1/getroles')
def get_roles():
    pass


@roles_bp.route('/roles/v1/createrole', methods=['POST'])
def create_role():

    roles_request = request.get_json()
    roles_request_name = roles_request['role_name']

    role = RolesModel(roles_request_name)

    db.session.add(role)
    db.session.commit()
    db.session.close()

    return jsonify(role), 200

    




