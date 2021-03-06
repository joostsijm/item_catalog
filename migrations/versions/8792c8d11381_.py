"""empty message

Revision ID: 8792c8d11381
Revises: 0ac4d2ac297e
Create Date: 2018-09-30 01:21:20.138104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8792c8d11381'
down_revision = '0ac4d2ac297e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('item', sa.Column('app_user_id', sa.Integer(), nullable=True))
    op.execute("INSERT INTO app_user VALUES(nextval('app_user_id_seq'::regclass), 'Admin', 'admin@admin.com')")
    op.execute("UPDATE item SET app_user_id=1")
    op.alter_column('item', 'app_user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key('item_app_user_id_fkey', 'item', 'app_user', ['app_user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('item_app_user_id_fkey', 'item', type_='foreignkey')
    op.drop_column('item', 'app_user_id')
    op.drop_table('app_user')
    # ### end Alembic commands ###
