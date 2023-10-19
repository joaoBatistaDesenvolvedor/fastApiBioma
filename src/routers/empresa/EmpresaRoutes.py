from fastapi import APIRouter
from src.controllers.empresa.EmpresaController import EmpresaController
from src.models.pydantic.models import EmpresaBase, EmpresaResponse, ErrorResponse, FindAllResponse, UpdateResponse, DeleteResponse,EmpresaUpdateResquest

router = APIRouter()
@router.post("/empresa", response_model=EmpresaResponse | ErrorResponse)
def create(dados: EmpresaBase) -> EmpresaResponse:
    return EmpresaController.create(dados)
@router.get("/empresa/{cnpj}", response_model=EmpresaResponse | ErrorResponse)
def get(cnpj: str) -> EmpresaResponse:
    return EmpresaController.get(cnpj)
@router.get("/empresa", response_model=FindAllResponse | ErrorResponse)
def get_all() -> FindAllResponse:
    return EmpresaController.get_all()
@router.delete("/empresa/{cnpj}", response_model=DeleteResponse | ErrorResponse)    
def delete(cnpj: str) -> DeleteResponse:
    return EmpresaController.delete(cnpj)
@router.put("/empresa/{cnpj}", response_model=UpdateResponse | ErrorResponse)
def update(cnpj: str, dados: EmpresaUpdateResquest) -> UpdateResponse:
    return EmpresaController.update(cnpj, dados)
