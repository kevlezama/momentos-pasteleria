from app.dbconfig import db

from sqlalchemy.orm import Mapped, mapped_column

import uuid
import datetime


class RolesModel(db.Model):
    
    __table__ = 'roles_model'

    roles_uid:Mapped[str] = mapped_column(
        init=False,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4)
    
    role_name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True)


    