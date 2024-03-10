"""add content column to posts table

Revision ID: 19a3175a4afb
Revises: 56c5f9482a8c
Create Date: 2024-03-08 23:20:42.785418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19a3175a4afb'
down_revision: Union[str, None] = '56c5f9482a8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
