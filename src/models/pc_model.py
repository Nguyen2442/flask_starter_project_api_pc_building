from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.config.config import db


class Component(db.Model):
    __tablename__ = 'components'
    part_id = db.Column(db.Integer, db.ForeignKey('parts.id'), primary_key=True)
    pc_id = db.Column(db.Integer, db.ForeignKey('pcs.id'), primary_key=True)
    quantity = db.Column(db.Integer, default=1)

    part = db.relationship("Part", foreign_keys=[part_id])

    def __init__(self, part_id,pc_id, quantity):
        self.part_id = part_id
        self.pc_id = pc_id
        self.quantity = quantity

    def format(self):
        return {
            'part_id': self.part_id,
            'pc_id': self.pc_id,
            'quantity': self.quantity
        }



class PC(db.Model):
    __tablename__ = 'pcs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer, default=0)
    userId_created = db.Column(db.Integer, db.ForeignKey('users.id'))


    components = db.relationship('Component', lazy=True, foreign_keys='Component.pc_id')
    

    def __init__(self, name, price, userId_created):
        self.name = name
        self.price = price
        self.userId_created = userId_created



    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'userId_created': self.userId_created
        }


