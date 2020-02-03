import datetime
import sqlalchemy
from sqlalchemy import orm

from data.models.rentals import Rental
from data.sqlalchemybase import SqlAlchemyBase


class Schedule(SqlAlchemyBase):
    __tablename__ = 'trains'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    departure_time = sqlalchemy.Column(sqlalchemy.Time, nullable=False index=True)
    travel_duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)


    train = sqlalchemy.Column(sqlalchemy.Integer,
                            sqlalchemy.ForeignKey('trains.id'),
                            nullable=False)

    orig_station = sqlalchemy.Column(sqlalchemy.Integer,
                            sqlalchemy.ForeignKey('stations.id'),
                            nullable=False)

    dest_station = sqlalchemy.Column(sqlalchemy.Integer,
                            sqlalchemy.ForeignKey('stations.id'),
                            nullable=False)
    
    
    station = orm.relation('Station')
    train = orm.relation('Train')