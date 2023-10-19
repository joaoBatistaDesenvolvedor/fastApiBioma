"""cria a tabela tabela colaborador

Revision ID: c4d6ee40688a
Revises: 7915f8b39d32
Create Date: 2023-10-17 17:59:46.284167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4d6ee40688a'
down_revision: Union[str, None] = '7915f8b39d32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   
    op.create_table(
        'Colaboradores',
        sa.Column('ColaboradorID', sa.Integer, primary_key=True),
        sa.Column('Nome', sa.String(255), nullable=False),
        sa.Column('CPF', sa.String(11), nullable=False, unique=True),
        sa.Column('Email', sa.String(255), nullable=False, unique=True),
        sa.Column('Senha', sa.String(255), nullable=False),
        sa.Column('Cargo', sa.String(255)),
        sa.Column('EmpresaID', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['EmpresaID'], ['Empresas.EmpresaID'], ),
        sa.PrimaryKeyConstraint('ColaboradorID')
        
    )


def downgrade() -> None:
    op.drop_table('Colaboradores')
