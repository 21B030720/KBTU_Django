"""try to create tables 2  migrations

Revision ID: 4aa84d1f7d11
Revises: 2fb02ee380ad
Create Date: 2024-05-18 10:55:16.522991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4aa84d1f7d11'
down_revision: Union[str, None] = '2fb02ee380ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
