from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
base=declarative_base()

class Empresa(base):
    __tablename__ = 'Empresas'
    EmpresaID = Column(Integer, primary_key=True)
    Nome = Column(String(255), nullable=False)
    CNPJ = Column(String(14), nullable=False, unique=True)
    Descricao = Column(String(255))
    
class Produto(base):
    __tablename__ = 'Produtos'
    ProdutoID = Column(Integer, primary_key=True)
    Nome = Column(String(255), nullable=False)
    Valor = Column(Float, nullable=False)
    Descricao = Column(String(255))
    Quantidade = Column(Integer)
    EmpresaID = Column(Integer, ForeignKey('Empresas.EmpresaID'))
    Empresa = relationship('Empresa')
    
class Colaborador(base):
        __tablename__ = 'Colaboradores'
        ColaboradorID = Column(Integer, primary_key=True)
        Nome = Column(String(255), nullable=False)
        CPF = Column(String(11), nullable=False, unique=True)
        Email = Column(String(255), nullable=False, unique=True)
        Senha = Column(String(255), nullable=False)
        Cargo = Column(String(255))
        EmpresaID = Column(Integer, ForeignKey('Empresas.EmpresaID'))
        Empresa = relationship('Empresa')
    
    