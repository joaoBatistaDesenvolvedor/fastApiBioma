from src.models.database.models import Produto
from src.configs.conection import *
from sqlalchemy.exc import SQLAlchemyError
from src.repositorys.empresa.EmpresaRepository import EmpresaRepository
class ProdutoRepository:
    def create(self, dados: Produto) -> Produto:
        
        try:
            
            with SessionLocal() as db:
                dados = Produto(**dados.dict())
                db.add(dados)
                db.commit()
                db.refresh(dados)
                return dados
        except SQLAlchemyError as e:
            print(str(e))
            
            return None
    def get(self,cod: int) -> Produto:
        try:
            with SessionLocal() as db:
                return db.query(Produto).filter(Produto.ProdutoID == cod).first()
        except:
            return None
    def get_all(self) -> list[Produto]:
        try:
            with SessionLocal() as db:
                
                return db.query(Produto).all()
            
        except SQLAlchemyError as e:
            return None
    def update(self,id: int, dados: Produto):
        
        try:
            with SessionLocal() as db:
                produto = db.query(Produto).filter(Produto.ProdutoID == id).first()
                if produto:
                    # Atualiza os dados da empresa apenas se o valor não for None
                    for key, value in dados.items():
                        if value is not None:
                            setattr(produto, key, value)
                    db.commit()
                    return produto
                else:
                    return None
        except SQLAlchemyError as e:
            print(str(e))
            return None
        
    def delete(self, cod):
        try:
            with SessionLocal() as db:
             prouto =db.query(Produto).filter(Produto.ProdutoID == cod).first()
             if(prouto):
                db.delete(prouto)
                db.commit()
                return True
             else:
                return False
        except:
            return None
        
    def ListALLProductsByCompany(self, cnpj: str) -> list[Produto]:
        try:
            empresa=EmpresaRepository().get(cnpj)
            if(empresa):
                with SessionLocal() as db:
                    return db.query(Produto).filter(Produto.EmpresaID == empresa.EmpresaID).all()
            else:
                return None
        except SQLAlchemyError as e:
            print(str(e))
            return None
    def buy_products(self, cnpj: str,idProduto: int,quantidade: int) -> list[Produto]:
        #verifica se a empresa existe
        #verifica se o produto existe
        #vericar se o produto tem estoque quantidade passada tem na empresa
        empresa = EmpresaRepository().get(cnpj)
        if(not empresa):
            return -1
        with SessionLocal() as db:
            produto = db.query(Produto).filter(Produto.ProdutoID == idProduto).first()
            if(not produto):
                return -2
            if(produto.Quantidade < quantidade):
                return -3
            produto.Quantidade -= quantidade
            db.commit()
            return db.query(Produto).filter(Produto.EmpresaID == empresa.EmpresaID).all()
    
        
        
        
         