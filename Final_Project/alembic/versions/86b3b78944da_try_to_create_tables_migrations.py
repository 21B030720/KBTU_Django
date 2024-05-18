"""try to create tables  migrations

Revision ID: 86b3b78944da
Revises: d6e00060a646
Create Date: 2024-05-18 10:48:04.585566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86b3b78944da'
down_revision: Union[str, None] = 'd6e00060a646'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
