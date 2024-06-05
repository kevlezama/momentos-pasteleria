from dbconfig import db

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship, attribute_keyed_dict
from typing import Optional

import uuid
import datetime

class Client(db.Model):

    __tablename__ = 'client_model'

    ######## Mapped columns in DB ############

    client_uid: Mapped[uuid.UUID] = mapped_column(
        init=False,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    client_id: Mapped[int] = mapped_column(
        unique=True)
    
    client_name: Mapped[str] = mapped_column(
        String(40)
    )

    client_last_name: Mapped[str] = mapped_column(
        String(20)
    )

    client_email: Mapped[str] = mapped_column(
        String(30)
    )

    client_state:Mapped[str]
    client_city: Mapped[str]
    client_delivery_address: Mapped[str]
    client_created_timestamp: Mapped[datetime.datetime] = mapped_column (
        insert_default=datetime.datetime.now
    )

    # Relationship with order model
    orders: Mapped[Optional[Dict[str,"Orders"]]]= relationship(
        collection_class=attribute_keyed_dict("order_uid"),
        cascade="all, delete-orphan", back_populates='clients')
    
    # Relationship with address model
    address: Mapped[Optional[Dict[str,"Client_adress_model"]]]= relationship(
        collection_class=attribute_keyed_dict("adress_uid"),
        cascade="all, delete-orphan", back_populates='clients')

    def obj_to_dict(self):

        data_request ={
            
            "client_create_date":str(self.client_created_timestamp),
            "client_uid":self.client_uid,
            "client_id":self.client_id,
            "client_name":self.client_name,
            "client_last_name":self.client_last_name,
            "client_email":self.client_email,
            "client_state":self.client_state,
            "client_city":self.client_city,
            "address_1":self.client_delivery_address,
            
        }

        return data_request