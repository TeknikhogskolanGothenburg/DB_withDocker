from db import Base
import sqlalchemy as sa


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.String(100), nullable=False)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100), nullable=False)
    email = sa.Column(sa.String(100), nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, user_name={self.user_name}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})'
