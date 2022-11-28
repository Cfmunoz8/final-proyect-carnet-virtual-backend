"""empty message

Revision ID: eec5584335ec
Revises: fa93b3cb3943
Create Date: 2022-11-28 18:55:47.884574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eec5584335ec'
down_revision = 'fa93b3cb3943'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('rut',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('rut',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###