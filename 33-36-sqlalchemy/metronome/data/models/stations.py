import datetime
import sqlalchemy
from sqlalchemy import orm

#from data.models.rentals import Rental
from data.sqlalchemybase import SqlAlchemyBase


class Station(SqlAlchemyBase):
    __tablename__ = 'stations'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    contact_phone = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True, unique=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    


    """
    # noinspection PyUnresolvedReferences
    rentals = orm.relation("Rental", order_by=[
        Rental.start_time.desc(),
    ], back_populates='user')
    """
