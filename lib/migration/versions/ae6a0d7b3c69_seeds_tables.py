"""seeds tables

Revision ID: ae6a0d7b3c69
Revises: c8530ccb895b
Create Date: 2023-08-22 03:46:48.367766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae6a0d7b3c69'
down_revision: Union[str, None] = 'c8530ccb895b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###