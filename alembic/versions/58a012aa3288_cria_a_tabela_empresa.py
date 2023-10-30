"""cria a tabela empresa

Revision ID: 58a012aa3288
Revises: 
Create Date: 2023-10-17 17:54:14.605029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58a012aa3288'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        'Empresas',
        sa.Column('EmpresaID', sa.Integer, primary_key=True),
        sa.Column('Nome', sa.String(255), nullable=False),
        sa.Column('CNPJ', sa.String(14), nullable=False, unique=True),
        sa.Column('Descricao', sa.Text)
    )

def downgrade() -> None:
    op.drop_table('Empresas')
