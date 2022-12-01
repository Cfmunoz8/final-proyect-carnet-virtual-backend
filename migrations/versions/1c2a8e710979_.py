"""empty message

Revision ID: 1c2a8e710979
Revises: a729ed5eea6f
Create Date: 2022-12-01 01:32:51.387683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c2a8e710979'
down_revision = 'a729ed5eea6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('controls', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_of_control', sa.Date(), nullable=False))
        batch_op.drop_column('date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('controls', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DATE(), nullable=False))
        batch_op.drop_column('date_of_control')

    # ### end Alembic commands ###