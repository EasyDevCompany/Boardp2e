"""added token to user

Revision ID: 19b80aa10e9e
Revises: f52dd510bceb
Create Date: 2022-12-11 01:42:48.304320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19b80aa10e9e'
down_revision = 'f52dd510bceb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('review', 'raiting',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=1),
               existing_nullable=True)
    op.add_column('user', sa.Column('token', sa.String(), nullable=True))
    op.alter_column('user', 'raiting',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=1),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'raiting',
               existing_type=sa.Float(precision=1),
               type_=sa.REAL(),
               existing_nullable=True)
    op.drop_column('user', 'token')
    op.alter_column('review', 'raiting',
               existing_type=sa.Float(precision=1),
               type_=sa.REAL(),
               existing_nullable=True)
    # ### end Alembic commands ###