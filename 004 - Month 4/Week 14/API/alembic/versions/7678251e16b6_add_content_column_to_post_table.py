"""add content column to post table

Revision ID: 7678251e16b6
Revises: 87301e746eae
Create Date: 2024-07-20 18:48:15.947082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7678251e16b6'
down_revision: Union[str, None] = '87301e746eae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
