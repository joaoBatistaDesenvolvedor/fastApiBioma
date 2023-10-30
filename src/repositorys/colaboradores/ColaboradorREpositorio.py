from src.configs.conection import *
from src.models.database.models import Colaborador, Empresa
from sqlalchemy.exc import SQLAlchemyError
import bcrypt


class ColaboradorRepositorio:
  # repository
    def create(self, dados: Colaborador) -> Colaborador:
        try:
             with SessionLocal() as db:
                 dados =Colaborador(
                     Nome=dados.Nome,
                     CPF=dados.CPF,
                     Email=dados.Email,
                     Senha=bcrypt.hashpw(dados.Senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                     Cargo=dados.Cargo,
                     EmpresaID=dados.EmpresaID
                     
                     
                 )
                 db.add(dados)
                 db.commit()
                 db.refresh(dados)
                 return dados
        except SQLAlchemyError as e:
            print(str(e))
            if "UNIQUE constraint failed" in str(e):
                return -1
            else:
                return None

    def get(self,cpf: str) -> Colaborador:
        try:
            with SessionLocal() as db:
                return db.query(Colaborador).filter(Colaborador.CPF == cpf).first()
        except:
            return None
    def get_all(self) -> list[Colaborador]:
        try:
            with SessionLocal() as db:
                colaboradores=db.query(Colaborador).all()
                return colaboradores
        except:
            return None
        
       
    def getAllByEmpresa(self, cnpj: str) -> list[Colaborador]:
        try:
            with SessionLocal() as db:
                empresa = db.query(Empresa).filter(Empresa.CNPJ == cnpj).first()
                if empresa:
                   colaboradores=db.query(Colaborador).filter(Colaborador.EmpresaID == empresa.EmpresaID).all() 
                   if colaboradores:
                    return colaboradores
                   
                else:
                    return None
                
        except:
            return None
     
    def update(self,cpf: str, dados: Colaborador):
        try:
            with SessionLocal() as db:
                colaborador = db.query(Colaborador).filter(Colaborador.CPF == cpf).first()
                if colaborador:
                    # Atualiza os dados da empresa apenas se o valor não for None
                    for key, value in dados.__dict__.items():
                        if value is not None:
                            setattr(colaborador, key, value)
                    db.commit()
                    return colaborador
                else:
                    return None
        except:
            return None
    def delete(self, cpf):
        try:
            with SessionLocal() as db:
                #busca o colaborador por cpf e se ele existir exclui
                colaborador = db.query(Colaborador).filter(Colaborador.CPF == cpf).first()
                if colaborador:
                    db.delete(colaborador)
                    db.commit()
                    return True
                else:
                    return False
        except:
            return -1
    def getColaboradorByEmailAndPassword(self, email: str, password: str) -> Colaborador:
        try:
            with SessionLocal() as db:
                colaborador = db.query(Colaborador).filter(Colaborador.Email == email).first()
                if colaborador:
                    if bcrypt.checkpw(password.encode('utf-8'), colaborador.Senha.encode('utf-8')):
                        return colaborador
                    else:
                        return None
                else:
                    return None
        except:
            return None
  
    
         
    
            
        
    