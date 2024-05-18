"""try to create tables 3 migrations

Revision ID: 4817130c8a51
Revises: 582c1c1b0fba
Create Date: 2024-05-18 10:58:06.239361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4817130c8a51'
down_revision: Union[str, None] = '582c1c1b0fba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
