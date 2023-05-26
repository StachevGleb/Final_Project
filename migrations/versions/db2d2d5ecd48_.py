"""empty message

Revision ID: db2d2d5ecd48
Revises: 1127003d47f2
Create Date: 2023-05-24 02:32:00.267246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db2d2d5ecd48'
down_revision = '1127003d47f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.alter_column('artistname',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=45),
               existing_nullable=False)

    with op.batch_alter_table('painting', schema=None) as batch_op:
        batch_op.alter_column('paint_file',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=60),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('painting', schema=None) as batch_op:
        batch_op.alter_column('paint_file',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.alter_column('artistname',
               existing_type=sa.String(length=45),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
