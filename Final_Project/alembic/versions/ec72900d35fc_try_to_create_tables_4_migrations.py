"""try to create tables 4 migrations

Revision ID: ec72900d35fc
Revises: 4817130c8a51
Create Date: 2024-05-18 10:59:13.065373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec72900d35fc'
down_revision: Union[str, None] = '4817130c8a51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
