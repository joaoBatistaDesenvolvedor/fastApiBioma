from fastapi import APIRouter
from src.controllers.produtos.ProdutosController import ProdutoController
from src.models.pydantic.models import ErrorResponse,ProdutoResponse,UpdateResponse,DeleteResponse,FindOneResponse,FindAllResponse,ProdutoBase,ProdutoListResponse,ProdutoUpdateResquest,buy_products

router = APIRouter()

@router.post("/produtos", response_model=ProdutoResponse | ErrorResponse)
def create(dados: ProdutoBase) -> ProdutoResponse:
    return ProdutoController.create(dados)
@router.get("/produtos/{id}", response_model=ProdutoResponse | ErrorResponse)
def get(id: str) -> ProdutoResponse:
    return ProdutoController.get(id)
@router.get("/produtos", response_model=ProdutoListResponse | ErrorResponse)
def get_all() -> FindAllResponse:
    return ProdutoController.get_all()

@router.get("/produtos/empresa/{cnpj}", response_model=ProdutoListResponse | ErrorResponse)
def ListALLProductsByCompany(cnpj: str) -> ProdutoListResponse:
    return ProdutoController.ListALLProductsByCompany(cnpj)
@router.put("/produtos/{id}", response_model=UpdateResponse | ErrorResponse)
def update(id : int,dados: ProdutoUpdateResquest) -> UpdateResponse:
    return ProdutoController.update(id,dados)

@router.delete("/produtos/{id}", response_model=DeleteResponse | ErrorResponse)
   
def delete(id: str) -> DeleteResponse:
    return ProdutoController.delete(id)
@router.post("/produtos/comprar", response_model=UpdateResponse | ErrorResponse)
def buy_products(buy_products: buy_products) -> UpdateResponse:
    return ProdutoController.buy_products(buy_products)

    

