from app.dbconfig import db

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .client_model import Client

import uuid
import datetime

class Client_adress_model(db.Model):

    __tablename__ ='client_adress_model'

    ######## Mapped columns in DB ############

    adress_uid: Mapped[str] = mapped_column(
    init=False,
    primary_key=True,
    nullable=False,
    default=uuid.uuid4)

    address_client_id:Mapped[str] = mapped_column(ForeignKey("client_model.client_uid"))

    client_state:Mapped[str]
    client_city: Mapped[str]
    client_delivery_address: Mapped[str]
    client_postal_code: Mapped[str]
    client_created_timestamp: Mapped[datetime.datetime] = mapped_column (
        insert_default=datetime.datetime.now
    )

    ########### Relationships ##########
    
    # Relationship with client model
    clients_adress_relationship: Mapped["Client"] = relationship(back_populates="adresses")

    