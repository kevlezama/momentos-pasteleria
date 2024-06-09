from app.dbconfig import db

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, attribute_keyed_dict
from typing import List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    #from .orders import Orders
    from .addresses_model import Client_adress_model

import uuid
import datetime

class Client(db.Model):

    __tablename__ = 'client_model'

    ######## Mapped columns in DB ############

    client_uid: Mapped[str] = mapped_column(
        init=False,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    client_id: Mapped[int] = mapped_column(
        unique=True)
    
    client_name: Mapped[str] = mapped_column(
        String(60)
    )

    client_last_name: Mapped[str] = mapped_column(
        String(60)
    )

    client_email: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    client_user: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=True
        #default=client_email
    )

    #client_role: Mapped[str] = mapped_column(ForeignKey('roles_model.roles_uid'))

    client_pass:Mapped[str]

    client_created_timestamp: Mapped[datetime.datetime] = mapped_column(
        insert_default=datetime.datetime.now
    )
    
    client_state:Mapped[str]

    client_city:Mapped[str]

    #client_delivery_list_adresses: Mapped[str] = mapped_column(ForeignKey("client_adress_model.address_client_id"))

    #adresses: Mapped[List['Client_adress_model']] = relationship(back_populates="clients_adress_relationship")

    @property
    def get_client_user(self):
        pass
    
    @get_client_user.setter
    def get_client_user(self):
        pass
    
