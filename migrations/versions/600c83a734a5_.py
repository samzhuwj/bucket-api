"""empty message

Revision ID: 600c83a734a5
Revises: f567acee9009
Create Date: 2018-01-14 00:18:00.602574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '600c83a734a5'
down_revision = 'f567acee9009'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_token')
    # ### end Alembic commands ###