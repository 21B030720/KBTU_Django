"""try to create tables 3 migrations

Revision ID: 582c1c1b0fba
Revises: 4aa84d1f7d11
Create Date: 2024-05-18 10:56:49.570433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '582c1c1b0fba'
down_revision: Union[str, None] = '4aa84d1f7d11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
