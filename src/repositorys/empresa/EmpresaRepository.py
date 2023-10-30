from src.configs.conection import *
from src.models.database.models import Empresa

from sqlalchemy.exc import SQLAlchemyError

class EmpresaRepository:
    def create(self, dados: Empresa) -> Empresa:
            try:
                with SessionLocal() as db:
                    dados = Empresa(**dados.dict())
                    db.add(dados)
                    db.commit()
                    db.refresh(dados)
                    return dados
            except SQLAlchemyError as e:
                print(str(e))
                return None
                            
                
                
    def get(self,cnpj: str) -> Empresa:
           try:
               with SessionLocal() as db:
                   emp=db.query(Empresa).filter(Empresa.CNPJ == cnpj).first()
                   if emp is None:
                       return None
                   
                   return emp

           except SQLAlchemyError as e: print(str(e));
           return e
    def get_all(self) -> list[Empresa]:
            try:
                with SessionLocal() as db:
                    return db.query(Empresa).all()
            except:
                return None
    def update(self, cnpj, dados: dict):
        try:
            with SessionLocal() as db:
                empresa = db.query(Empresa).filter(Empresa.CNPJ == cnpj).first()
                if empresa:
                    # Atualiza os dados da empresa apenas se o valor não for None
                    for key, value in dados.items():
                        if value is not None:
                            setattr(empresa, key, value)
                    db.commit()
                    return empresa
                else:
                    return None
        except SQLAlchemyError as e:
            print(str(e))
            return None

    

                    
    def delete(self, cnpj: str) -> bool:
        try:
            with SessionLocal() as db:
                empresa = db.query(Empresa).filter(Empresa.CNPJ == cnpj).first()
                if empresa:
                    db.delete(empresa)
                    db.commit()
                    return True
                else:
                    return False
        except:
            return False
