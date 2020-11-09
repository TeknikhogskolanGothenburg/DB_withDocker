from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Parent(Base):
    __tablename__ = 'parents'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    children = relationship("Child", back_populates="parent")


    def __repr__(self):
        return f'{self.name}\nChildren:\n\t{"".join(child.name + ", " for child in self.children)}'
