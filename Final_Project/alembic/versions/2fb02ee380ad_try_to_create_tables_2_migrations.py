"""try to create tables 2  migrations

Revision ID: 2fb02ee380ad
Revises: 86b3b78944da
Create Date: 2024-05-18 10:54:30.927634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2fb02ee380ad'
down_revision: Union[str, None] = '86b3b78944da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
