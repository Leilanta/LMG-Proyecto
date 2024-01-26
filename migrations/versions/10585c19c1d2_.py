"""empty message

Revision ID: 10585c19c1d2
Revises: a43f68e7e6a1
Create Date: 2024-01-25 21:39:30.762489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10585c19c1d2'
down_revision = 'a43f68e7e6a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign', schema=None) as batch_op:
        batch_op.add_column(sa.Column('objetivo', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('articulos', sa.String(length=80), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign', schema=None) as batch_op:
        batch_op.drop_column('articulos')
        batch_op.drop_column('objetivo')

    # ### end Alembic commands ###
