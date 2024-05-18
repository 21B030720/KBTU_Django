"""try to create tables 4 migrations

Revision ID: 11f95ee587f5
Revises: ec72900d35fc
Create Date: 2024-05-18 10:59:41.248283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11f95ee587f5'
down_revision: Union[str, None] = 'ec72900d35fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
