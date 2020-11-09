from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Child(Base):
    __tablename__ = 'children'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey('parents.id'))
    parent = relationship("Parent", back_populates="children")


    def __repr__(self):
        return f'{self.name} has a parent named {self.parent.name}'
