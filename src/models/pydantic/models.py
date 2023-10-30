from pydantic import BaseModel
from typing import List, Optional

class EmpresaBase(BaseModel):
  
    Nome: str
    CNPJ: str
    Descricao: str

class EmpresaCreate(EmpresaBase):
     class Config:
        orm_mode = True



    

class ProdutoBase(BaseModel):
    Nome: str
    Valor: float
    Descricao: str
    Quantidade: int
    EmpresaID: int
    class Config:
            orm_mode = True

class ProdutoCreate(ProdutoBase):
    class Config:
        orm_mode = True
        
class EmpresaUpdate(BaseModel):
    Nome: Optional[str] = None
    CNPJ: Optional[str] = None
    Descricao: Optional[str] = None




class ColaboradorBase(BaseModel):
    Nome: str
    CPF: str
    Email: str
    Senha: str
    Cargo: str
    EmpresaID: int
    class Config:
            orm_mode = True

class ColaboradorCreate(ColaboradorBase):
 class Config:
        orm_mode = True
class ProdutoUpdate(BaseModel):
    Nome: Optional[str] = None
    Valor: Optional[float] = None
    Descricao: Optional[str] = None
    Quantidade: Optional[int] = None
    
class ColaboradorUpdate(BaseModel):
    Nome: Optional[str] = None
    CPF: Optional[str] = None
    Email: Optional[str] = None
    Senha: Optional[str] = None
    Cargo: Optional[str] = None
    EmpresaID: Optional[int] = None
    
    
class EmpresaListResponse(BaseModel):
    empresas: List[EmpresaBase]
    class Config:
        orm_mode = True
class ProdutoListResponse(BaseModel):
    data: List[ProdutoBase]
    class Config:
        orm_mode = True
class ColaboradorResponse(BaseModel):
    colaborador: dict
    class Config:
        orm_mode = True
class ColaboradorListResponse(BaseModel):
    colaboradores: List[ColaboradorResponse]
    class Config:
        orm_mode = True

class EmpresaResponse(BaseModel):
    empresa: EmpresaBase
    class Config:
        orm_mode = True
class ProdutoResponse(BaseModel):
    produto: ProdutoBase
    class Config:
        orm_mode = True
class ColaboradorResponse(BaseModel):
    colaborador: ColaboradorBase
    class Config:
        orm_mode = True
class ErrorResponse(BaseModel):
    status_code: int
    message: str
    where: Optional[str] = None
    class Config:
        orm_mode = True
        
class FindAllResponse(BaseModel):
    data: List
    class Config:
        orm_mode = True
        
class FindOneResponse(BaseModel):
    data: dict
    class Config:
        orm_mode = True
class UpdateResponse(BaseModel):
    data: dict
    class Config:
        orm_mode = True
class DeleteResponse(BaseModel):
    data: dict
    class Config:
        orm_mode = True
class EmpresaUpdateResquest(BaseModel):
    Nome: Optional[str] = None
    CNPJ: Optional[str] = None
    Descricao: Optional[str] = None
    class Config:
            orm_mode = True

class ProdutoUpdateResquest(BaseModel):
    Nome: Optional[str] = None
    Valor: Optional[float] = None
    Descricao: Optional[str] = None
    Quantidade: Optional[int] = None
    EmpresaID: int
    class Config:
            orm_mode = True
class buy_products(BaseModel):
    cnpj: str
    idProduto: int
    quantidade: int
    class Config:
        orm_mode = True
        
class ColaboradorUpdateResquest(BaseModel):
    Nome: Optional[str] = None
    CPF: Optional[str] = None
    Email: Optional[str] = None
    Senha: Optional[str] = None
    Cargo: Optional[str] = None
    EmpresaID: int
    class Config:
            orm_mode = True
class User(BaseModel):
    email: str
    password: str
    
class Token(BaseModel):
    access_token: str
    