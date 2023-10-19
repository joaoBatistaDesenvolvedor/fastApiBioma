from fastapi import APIRouter
from src.controllers.colaborador.colaboradorController import ColaboradorController
from src.models.pydantic.models import ColaboradorBase,ColaboradorResponse,ErrorResponse,FindAllResponse,DeleteResponse,UpdateResponse,ColaboradorListResponse,ColaboradorUpdateResquest,User,Token

router = APIRouter()

@router.post("/colaborador", response_model=ColaboradorResponse | ErrorResponse)
def create(dados: ColaboradorBase) -> ColaboradorResponse:
    return ColaboradorController.create(dados)
@router.get("/colaborador/{cpf}",response_model=ColaboradorResponse | ErrorResponse)
def get(cpf: str)->ColaboradorResponse:
    return ColaboradorController.get(cpf)
@router.get("/colaborador",response_model=FindAllResponse | ErrorResponse)
def get_all() -> FindAllResponse:
    return ColaboradorController.get_all()
@router.get("/colaborador/empresa/{cnpj}",response_model=FindAllResponse | ErrorResponse)
def getAllByEmpresa(cnpj: str) -> FindAllResponse:
    return ColaboradorController.getAllByEmpresa(cnpj)

@router.delete("/colaborador/{cpf}",response_model=DeleteResponse | ErrorResponse)
def delete(cpf: str)->DeleteResponse:
    return ColaboradorController.delete(cpf)
@router.put("/colaborador/{cpf}",response_model=UpdateResponse | ErrorResponse)
def update(cpf: str,dados: ColaboradorUpdateResquest)->UpdateResponse:
    return ColaboradorController.update(cpf,dados)
@router.post("/colaborador/logar",response_model=Token | ErrorResponse)
def getColaboradorByEmailAndPassword(User:User)->Token:
    return ColaboradorController.getColaboradorByEmailAndPassword(User)
