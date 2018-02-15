"""empty message

Revision ID: 5e59ad74cc88
Revises: 6fa406d605f9
Create Date: 2018-02-11 14:08:47.040510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e59ad74cc88'
down_revision = '6fa406d605f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('complaint', sa.Column('long_describtion', sa.String(), nullable=True))
    op.add_column('complaint', sa.Column('short_describtion', sa.String(length=280), nullable=True))
    op.drop_column('complaint', 'problem_summary')
    op.drop_column('complaint', 'problem_details')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('complaint', sa.Column('problem_details', sa.VARCHAR(), nullable=True))
    op.add_column('complaint', sa.Column('problem_summary', sa.VARCHAR(length=280), nullable=True))
    op.drop_column('complaint', 'short_describtion')
    op.drop_column('complaint', 'long_describtion')
    # ### end Alembic commands ###
