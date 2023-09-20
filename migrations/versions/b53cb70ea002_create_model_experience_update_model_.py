"""create model experience, update model contacts

Revision ID: b53cb70ea002
Revises: 
Create Date: 2023-09-20 15:27:50.789836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b53cb70ea002'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('experience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact_name', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('contact_value', sa.String(length=255), nullable=True))
        batch_op.drop_constraint('contacts_email_key', type_='unique')
        batch_op.drop_constraint('contacts_phone_key', type_='unique')
        batch_op.drop_column('site')
        batch_op.drop_column('linkedin')
        batch_op.drop_column('phone')
        batch_op.drop_column('email')
        batch_op.drop_column('git')
        batch_op.drop_column('telegram')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telegram', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('git', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('phone', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('linkedin', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('site', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('contacts_phone_key', ['phone'])
        batch_op.create_unique_constraint('contacts_email_key', ['email'])
        batch_op.drop_column('contact_value')
        batch_op.drop_column('contact_name')

    op.drop_table('experience')
    # ### end Alembic commands ###
