"""try to create tables 4 migrations

Revision ID: 614b43909804
Revises: 11f95ee587f5
Create Date: 2024-05-18 11:00:13.805881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '614b43909804'
down_revision: Union[str, None] = '11f95ee587f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
