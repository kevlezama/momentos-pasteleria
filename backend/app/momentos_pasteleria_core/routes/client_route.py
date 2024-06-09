# Flask framework
from flask import Blueprint, request, jsonify

# Sqlalchemy ORM API
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

# Global config dependencies
from app.dbconfig import db
from models.client_model import Client

# Python buildin
import uuid
import datetime
import json
import logging

client_bp  = Blueprint('clients', __name__)

CLIENTS_ORDER_BY_CLIENT_ID_STM = select(Client).order_by(Client.client_id)

@client_bp .route('/clients/getall/clients', methods=['GET'])
def get_all_clients():
    query_execution = db.session.execute(CLIENTS_ORDER_BY_CLIENT_ID_STM).all()
    #clients = Client.query.all()
    #with db.session as session:
    #    for row in session.execute(CLIENTS_ORDER_BY_CLIENT_ID_STM):
    #        print(row)
    #return clients
    return query_execution

@client_bp .route('/clients/createclient', methods=['POST'])
def create_new_client():

    request_data = request.get_json()
    clt_email = request_data['client_email']
    logging.info('POST request: ' + clt_email)

    try:
        stm_get_client_email = select(Client).where(Client.client_email==clt_email)
        exec_stm = db.session.execute(stm_get_client_email).one_or_none()
        logging.info('-------------- START HERE ------------------')
        data_load = None

    except MultipleResultsFound as e:

        return e

@client_bp .route('/clients/createclient', methods=['POST'])
def create_new_client() -> any:

    request_data = request.get_json()
    
    clt_id = request_data['client_id']
    clt_name = request_data['client_name'] 
    clt_last_name = request_data['client_last_name']
    clt_email = request_data['client_email']
    clt_state =  request_data['client_state']
    clt_city = request_data['client_city']
    clt_delivery_addres = request_data['client_delivery_address']
    clt_addrs = {}
    clt_orders = {}
    user_created_data_timestamp = datetime.datetime.now()

    client = Client(
        #user_uuid,
        clt_id,
        clt_name,
        clt_last_name,
        clt_email,
        clt_state,
        clt_city,
        clt_delivery_addres,
        user_created_data_timestamp,
        clt_orders,
        clt_addrs
        )
    
    db.session.add(client)
    db.session.commit()

    return jsonify(client), 200


