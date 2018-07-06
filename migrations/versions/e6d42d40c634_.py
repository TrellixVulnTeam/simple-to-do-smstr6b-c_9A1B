"""empty message

Revision ID: e6d42d40c634
Revises: be1d2a91384e
Create Date: 2018-07-05 11:17:49.793527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6d42d40c634'
down_revision = 'be1d2a91384e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('buku', sa.Column('created_at', sa.DATETIME(), nullable=True))
    op.add_column('buku', sa.Column('updated_at', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('buku', 'updated_at')
    op.drop_column('buku', 'created_at')
    # ### end Alembic commands ###
