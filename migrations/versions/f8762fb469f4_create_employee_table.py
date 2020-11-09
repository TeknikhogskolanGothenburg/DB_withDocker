"""Create Employee Table

Revision ID: f8762fb469f4
Revises: 859f6ce11c65
Create Date: 2020-11-09 11:47:00.129281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8762fb469f4'
down_revision = '859f6ce11c65'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100))
    )


def downgrade():
    op.drop_table('employees')
