import datetime
import sqlalchemy
from sqlalchemy import orm

from data.models.rentals import Rental
from data.sqlalchemybase import SqlAlchemyBase


class Train(SqlAlchemyBase):
    __tablename__ = 'trains'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    model = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    manufacture_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    capacity = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    default_station = sqlalchemy.Column(sqlalchemy.Integer,
                            sqlalchemy.ForeignKey('stations.id'),
                            nullable=False)

    current_station = sqlalchemy.Column(sqlalchemy.Integer,
                            sqlalchemy.ForeignKey('stations.id'),
                            nullable=False)
    
    
    station = orm.relation('Station')