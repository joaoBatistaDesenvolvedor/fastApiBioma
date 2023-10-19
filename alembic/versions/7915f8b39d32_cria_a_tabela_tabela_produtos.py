"""cria a tabela tabela produtos

Revision ID: 7915f8b39d32
Revises: 58a012aa3288
Create Date: 2023-10-17 17:57:44.465104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7915f8b39d32'
down_revision: Union[str, None] = '58a012aa3288'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

  
  op.create_table(
    'Produtos',
    sa.Column('ProdutoID', sa.Integer, primary_key=True),
    sa.Column('Nome', sa.String(255), nullable=False),
    sa.Column('Valor', sa.Float, nullable=False),
    sa.Column('Descricao', sa.Text),
    sa.Column('Quantidade', sa.Integer),
    sa.Column('EmpresaID', sa.Integer, nullable=False),
    sa.ForeignKeyConstraint(['EmpresaID'], ['Empresas.EmpresaID'], ),
    sa.PrimaryKeyConstraint('ProdutoID')
  )


def downgrade() -> None:
  op.drop_table('Produtos')
    
