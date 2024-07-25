"""test phone number

Revision ID: c862ddfaf8d3
Revises: 113a2fe9b9ad
Create Date: 2024-07-23 19:47:24.313345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c862ddfaf8d3'
down_revision: Union[str, None] = '113a2fe9b9ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
