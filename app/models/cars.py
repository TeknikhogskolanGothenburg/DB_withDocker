from db import Base
import sqlalchemy as sa


class Car(Base):
    __tablename__ = 'cars'

    id = sa.Column(sa.Integer, primary_key=True)
    brand = sa.Column(sa.String(100), nullable=False)
    model = sa.Column(sa.String(100), nullable=False)
    year = sa.Column(sa.String(4), nullable=False)


    def __repr__(self):
        return f'Car(id={self.id}, brand={self.brand}, model={self.model}, year={self.year})'
