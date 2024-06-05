from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from flask_sqlalchemy import SQLAlchemy

# Configuration of ORM DB models 
class Base(DeclarativeBase, MappedAsDataclass):
  pass

db = SQLAlchemy(model_class=Base)
