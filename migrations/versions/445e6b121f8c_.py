"""Alter password to binary data

Revision ID: 445e6b121f8c
Revises: f1bf5ec74d0a
Create Date: 2023-11-05 18:29:25.789708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '445e6b121f8c'
down_revision = 'f1bf5ec74d0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.LargeBinary(),
               existing_nullable=True,
               postgresql_using='password::bytea')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.LargeBinary(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
