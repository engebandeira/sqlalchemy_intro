"""primeira

Revision ID: 29ea3e1d463b
Revises: 
Create Date: 2025-06-26 11:19:01.025887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '29ea3e1d463b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column('id',sa.Integer(),primary_key=True),
        sa.Column('nome',sa.String(length=50),nullable=False),
        sa.Column('email',sa.String(length=50),nullable=False)
    )


def downgrade() -> None:
    op.drop_table('pessoa')
    