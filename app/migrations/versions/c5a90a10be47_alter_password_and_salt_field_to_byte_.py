"""alter password and salt field to byte, added token

Revision ID: c5a90a10be47
Revises: a8353ba6db50
Create Date: 2022-12-10 02:04:37.184483

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from app.utils.bytes_field import HexByteString

# revision identifiers, used by Alembic.
revision = 'c5a90a10be47'
down_revision = 'a8353ba6db50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_token',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id')
    )
    op.create_index(op.f('ix_user_token_id'), 'user_token', ['id'], unique=False)
    op.alter_column('review', 'raiting',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=1),
               existing_nullable=True)
    op.add_column('user', sa.Column('salt', HexByteString(), nullable=True))
    op.alter_column('user', 'raiting',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=1),
               existing_nullable=True)
    op.create_unique_constraint(None, 'user', ['login'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'raiting',
               existing_type=sa.Float(precision=1),
               type_=sa.REAL(),
               existing_nullable=True)
    op.drop_column('user', 'salt')
    op.alter_column('review', 'raiting',
               existing_type=sa.Float(precision=1),
               type_=sa.REAL(),
               existing_nullable=True)
    op.drop_index(op.f('ix_user_token_id'), table_name='user_token')
    op.drop_table('user_token')
    # ### end Alembic commands ###