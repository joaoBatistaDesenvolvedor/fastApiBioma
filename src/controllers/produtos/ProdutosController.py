from src.repositorys.produtos.ProdutoRepository import ProdutoRepository
from src.models.pydantic.models import ErrorResponse,ProdutoResponse,UpdateResponse,DeleteResponse,FindOneResponse,FindAllResponse,ProdutoBase,ProdutoListResponse,ProdutoUpdateResquest,buy_products

class ProdutoController:
    @staticmethod
    def create(dados: ProdutoBase) -> ProdutoResponse:
        repository = ProdutoRepository()
        try:
            if(dados.Nome is None and dados.Valor is None and dados.Descricao is None):
                return ErrorResponse(status_code=400, message="dados não informados por informe os dados necessários", where="create")
            
            repository.create(dados)
            return ProdutoResponse(produto=dados)
        except:
            return ErrorResponse(status_code=500, message="Erro ao cadastrar produtoador", where="create")
    @staticmethod
    def get(id: int) -> ProdutoResponse:
        repository = ProdutoRepository()
        try:
            produto=repository.get(id)
            return ProdutoResponse(produto=ProdutoBase(
                Nome=produto.Nome,
                Valor=produto.Valor,
                Descricao=produto.Descricao,
                Quantidade=produto.Quantidade,
                EmpresaID=produto.EmpresaID
            ))
            
        except:
            return ErrorResponse(status_code=500, message="Erro ao buscar produto", where="get")
    @staticmethod
    def get_all() -> ProdutoListResponse:
        repository = ProdutoRepository()
        try:
   
            produtos=repository.get_all()
            base=[]
            for produto in produtos:
                base.append(ProdutoBase(
                    Nome=produto.Nome,
                    Valor=produto.Valor,
                    Descricao=produto.Descricao,
                    Quantidade=produto.Quantidade,
                    EmpresaID=produto.EmpresaID
                ))
            return ProdutoListResponse(data=base)
        except:
            return ErrorResponse(status_code=500, message="Erro ao buscar todos os produtoadores", where="get_all")
    def ListALLProductsByCompany(cnpj:str)->ProdutoListResponse:
        repository = ProdutoRepository()
        try:
            produtos=repository.ListALLProductsByCompany(cnpj)
            base=[]
            for produto in produtos:
                base.append(ProdutoBase(
                    Nome=produto.Nome,
                    Valor=produto.Valor,
                    Descricao=produto.Descricao,
                    Quantidade=produto.Quantidade,
                    EmpresaID=produto.EmpresaID
                ))
            return ProdutoListResponse(data=base)
        except:
            return ErrorResponse(status_code=500, message="Erro ao buscar todos os produtos", where="ListALLProductsByCompany")
            
    def update(id: int,dados: ProdutoUpdateResquest) -> UpdateResponse:
       
        try:
                 if(dados.Nome is None and dados.Valor is None and dados.Descricao is None and dados.Quantidade is None and dados.EmpresaID is None):
                    return ErrorResponse(status_code=400, message="dados não informados por informe os dados necessários", where="update")
                 repository = ProdutoRepository()
                 data_dict = dados.dict()
                 repository.update(id,data_dict)
                 
                 
                 return UpdateResponse(data={"message": "Produto atualizado com sucesso"})
        except:
                    return ErrorResponse(status_code=500, message="Erro ao atualizar produto", where="update")
                
    def delete(id: int) -> DeleteResponse:
                try:
                    repository = ProdutoRepository()
                    produto=repository.delete(id)
                    if(produto):
                       return DeleteResponse(data={"message": "Produto deletado com sucesso"})
                    else:
                        return ErrorResponse(status_code=404, message="Produto nao encontrado", where="delete")
                    
                except:
                    return ErrorResponse(status_code=500, message="Erro ao deletar produto", where="delete")
                
    def buy_products(buy_products: buy_products)->UpdateResponse:
        try:
          repository=ProdutoRepository()
          produto= repository.buy_products(buy_products.cnpj,buy_products.idProduto,buy_products.quantidade)
          if(produto==-1):
              return ErrorResponse(status_code=404, message="empresa nao encontrada", where="buy_products")
          elif(produto==-2):
              return ErrorResponse(status_code=404, message="produto nao encontrado", where="buy_products")
          elif(produto==-3):
              return ErrorResponse(status_code=404, message="quantidade invalida", where="buy_products")
          else:
              return UpdateResponse(data={"message": "Produto comprado com sucesso"})
          
        except:
            return ErrorResponse(status_code=500, message="Erro ao comprar produto", where="buy_products")
        