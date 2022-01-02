"""empty message

Revision ID: 938f5de720a7
Revises: 079b33409ec1
Create Date: 2021-12-31 17:34:09.597268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '938f5de720a7'
down_revision = '079b33409ec1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('is_released', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'is_released')
    # ### end Alembic commands ###