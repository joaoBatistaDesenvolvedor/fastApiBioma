from src.repositorys.colaboradores.ColaboradorREpositorio import ColaboradorRepositorio
from src.models.pydantic.models import ColaboradorResponse,ColaboradorBase,UpdateResponse,DeleteResponse,FindOneResponse,FindAllResponse,ErrorResponse,ColaboradorUpdateResquest,User,Token
from src.configs.jwt import token
from sqlalchemy.exc import IntegrityError

class ColaboradorController:
    @staticmethod
    def create(dados: ColaboradorBase) -> ColaboradorResponse:
            try:
                colaborador=ColaboradorRepositorio()
                if(dados.Nome is None and dados.CPF is None and dados.Email is None and dados.Senha is None and dados.Cargo is None and dados.EmpresaID is None):
                    return ErrorResponse(status_code=400, message="Dados não informados por informe os dados necessários", where="create")
                
                colaborador.create(dados)
                if colaborador == -1:
                    return ErrorResponse(status_code=400, message="CPF já existe", where="create")
                return ColaboradorResponse(colaborador=dados)
            except IntegrityError as error:
                    return ErrorResponse(status_code=400, message=error, where="create")
                
            except:
                return ErrorResponse(status_code=500, message="Erro ao cadastrar colaborador", where="create")
            
        


    @staticmethod
    def get(cpf: str) -> ColaboradorResponse:
        repository = ColaboradorRepositorio()
        try:
            colaborador = repository.get(cpf)
            return ColaboradorResponse(colaborador=ColaboradorBase(
                Nome=colaborador.Nome,
                CPF=colaborador.CPF,
                Email=colaborador.Email,
                Cargo=colaborador.Cargo,
                Senha=colaborador.Senha,
                EmpresaID=colaborador.EmpresaID
                
            ))
        except:
            return ErrorResponse(status_code=404, message="Colaborador não encontrado", where="get")
        
    def getAllByEmpresa(cnpj: str) -> FindAllResponse:
        repository = ColaboradorRepositorio()
        try:
            colaboradores = repository.getAllByEmpresa(cnpj)
            base=[]
            
            for colaborador in colaboradores:
                base.append(ColaboradorBase(
                    
                    Nome=colaborador.Nome,
                    CPF=colaborador.CPF,
                    Email=colaborador.Email,
                    Cargo=colaborador.Cargo,
                    Senha=colaborador.Senha,
                    EmpresaID=colaborador.EmpresaID
                ))
            return FindAllResponse(data=base)
        except:
            return ErrorResponse(status_code=500, message="Erro ao buscar todos os colaboradores", where="getAllByEmpresa")
    @staticmethod
    def get_all() -> FindAllResponse:
        repository = ColaboradorRepositorio()
        try:
            colaboradores = repository.get_all()
            base=[]
            for colaborador in colaboradores:
                base.append(ColaboradorBase(
                    
                    Nome=colaborador.Nome,
                    CPF=colaborador.CPF,
                    Email=colaborador.Email,
                    Cargo=colaborador.Cargo,
                    Senha=colaborador.Senha,
                    EmpresaID=colaborador.EmpresaID
                ))
            return FindAllResponse(data=base)
        except:
            return ErrorResponse(status_code=500, message="Erro ao buscar todos os colaboradores", where="get_all")
        
        
    @staticmethod
    def update(cpf: str, dados: ColaboradorUpdateResquest) -> UpdateResponse:
        repository = ColaboradorRepositorio()
        try:
            sucess = repository.update(cpf, dados)
            if sucess:
                return UpdateResponse(data={"message": "Colaborador atualizado com sucesso"})
            else:
                return ErrorResponse(status_code=404, message="Colaborador não encontrado", where="update")
        except:
            return ErrorResponse(status_code=500, message="Erro ao atualizar colaborador", where="update")
    @staticmethod
    def delete(cpf: str) -> DeleteResponse:
        repository = ColaboradorRepositorio()
        try:
            sucess = repository.delete(cpf)
            if sucess:
                return DeleteResponse(data={"message": "Colaborador deletado com sucesso"})
            else:
                return ErrorResponse(status_code=404, message="Colaborador não encontrado", where="delete")
        except:
            return ErrorResponse(status_code=500, message="Erro ao deletar colaborador", where="delete")
    def getColaboradorByEmailAndPassword(User:User) -> Token:
        repository = ColaboradorRepositorio()
        try:
            colaborador = repository.getColaboradorByEmailAndPassword(User.email, User.password)
       
            if(colaborador):
                token_user= token.generate_jwt_token(colaborador.CPF, colaborador.Nome)
                return Token(access_token=token_user)
            if(not colaborador):
                return ErrorResponse(status_code=404, message="Colaborador nao encontrado", where="getColaboradorByEmailAndPassword")
            
        except:
            return ErrorResponse(status_code=404, message="Colaborador não encontrado", where="getColaboradorByEmailAndPassword")
        
        
    