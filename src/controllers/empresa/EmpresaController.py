from src.repositorys.empresa.EmpresaRepository import EmpresaRepository
from src.models.pydantic.models import ErrorResponse,EmpresaResponse,UpdateResponse,DeleteResponse,FindOneResponse,FindAllResponse,EmpresaBase,EmpresaUpdateResquest
from src.models.database.models import Empresa
from fastapi import HTTPException

class EmpresaController:
    @staticmethod
    def create(dados: EmpresaBase) -> EmpresaResponse:
        repository = EmpresaRepository()
        if(dados.Nome is None and dados.CNPJ is None and dados.Descricao is None):
            return ErrorResponse(status_code=400, message="Dados não informados por informe os dados necessários", where="create")
        try:
            repository.create(dados)
            return EmpresaResponse(empresa=dados)
        except:
            return ErrorResponse(status_code=500, message="Erro ao cadastrar empresa", where="create")
    def get(cnpj: str) -> EmpresaResponse:
        repository = EmpresaRepository()
        empresa = repository.get(cnpj)
        if empresa:
            empresa_base = EmpresaBase(
                Nome=empresa.Nome,
                CNPJ=empresa.CNPJ,
                Descricao=empresa.Descricao
            )
            return EmpresaResponse(empresa=empresa_base)
        return ErrorResponse(status_code=404, message="Empresa não encontrada", where="get")
    
    @staticmethod
    def get_all() -> FindAllResponse:
            repository = EmpresaRepository()
            try:
                empresa_bases = []
                empresas = repository.get_all()
                for empresa in empresas:
                    empresa_bases.append(EmpresaBase(
                        Nome=empresa.Nome,
                        CNPJ=empresa.CNPJ,
                        Descricao=empresa.Descricao
                    ))
                    
                return FindAllResponse(data=empresa_bases)
            except:
                return ErrorResponse(status_code=500, message="Erro ao buscar todas as empresas", where="get_all")
                    
        
    @staticmethod
    def update(cnpj: str, dados: EmpresaUpdateResquest) -> UpdateResponse:
        repository = EmpresaRepository()
        try:
            if(dados.Nome is None and dados.CNPJ is None and dados.Descricao is None):
                return ErrorResponse(status_code=400, message="é informar pelo menos um valor", where="update")
            
            # Converte os dados de EmpresaBase para um dicionário
            dados_dict = dados.dict()

            # Chama o método de atualização no repositório
            empresa_updated = repository.update(cnpj, dados_dict)

            if empresa_updated:
                return UpdateResponse(data={"message": "Empresa atualizada com sucesso"})
            else:
                return ErrorResponse(status_code=404, message="Empresa não encontrada", where="update")

        except:
            return ErrorResponse(status_code=500, message="Erro ao atualizar empresa", where="update")

        
    @staticmethod
    def delete(cnpj: str) -> DeleteResponse:
        repository = EmpresaRepository()
        try:
            success = repository.delete(cnpj)
            if success:
                return DeleteResponse(data={"message": "Empresa deletada com sucesso"})
            else:
                raise HTTPException(status_code=404, detail="Empresa não encontrada")
        except:
            raise HTTPException(status_code=500, detail="Erro ao deletar empresa")
            
