"""empty message

Revision ID: 1a13991a5b75
Revises: a5cc01a147ca
Create Date: 2021-12-31 16:22:47.887965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a13991a5b75'
down_revision = 'a5cc01a147ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cascadeur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('actor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cascadeur_is_active'), 'cascadeur', ['is_active'], unique=False)
    op.create_index(op.f('ix_cascadeur_name'), 'cascadeur', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cascadeur_name'), table_name='cascadeur')
    op.drop_index(op.f('ix_cascadeur_is_active'), table_name='cascadeur')
    op.drop_table('cascadeur')
    # ### end Alembic commands ###