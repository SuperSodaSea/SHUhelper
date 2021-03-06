"""empty message

Revision ID: 231c8e177583
Revises: f0e7e6e9f4c2
Create Date: 2018-05-21 18:40:15.701078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '231c8e177583'
down_revision = 'f0e7e6e9f4c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('graduate_student',
    sa.Column('id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('undergraduate_student',
    sa.Column('id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('undergraduate_student')
    op.drop_table('graduate_student')
    # ### end Alembic commands ###
