import datetime

import sqlalchemy as sa
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class Track(SqlAlchemyBase):
    __tablename__ = 'tracks'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    state = sa.Column(sa.String, nullable=True)

    station_a = sa.Column(sa.Integer,
                            sa.ForeignKey('stations.id'),
                            nullable=False)

    station_a = sa.Column(sa.Integer,
                            sa.ForeignKey('stations.id'),
                            nullable=False)
    
    station = orm.relation('Station')
