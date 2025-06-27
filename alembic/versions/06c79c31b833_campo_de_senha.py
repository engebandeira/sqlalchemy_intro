"""campo de senha

Revision ID: 06c79c31b833
Revises: 29ea3e1d463b
Create Date: 2025-06-26 15:59:10.065246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06c79c31b833'
down_revision: Union[str, Sequence[str], None] = '29ea3e1d463b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('pessoa', sa.Column('senha', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('pessoa', 'senha')
    # ### end Alembic commands ###