"""Create StoreEmployee  Table

Revision ID: 1e6699d02b8d
Revises: f8762fb469f4
Create Date: 2020-11-09 11:50:09.233703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e6699d02b8d'
down_revision = 'f8762fb469f4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stores_employees',
        sa.Column('id',sa.Integer, primary_key=True),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.id')),
        sa.Column('store_id', sa.Integer, sa.ForeignKey('stores.id'))
    )


def downgrade():
    op.drop_table('stores_employees')
