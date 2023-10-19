from fastapi import FastAPI
from src.routers.colaborador import colaboradorRoutes
from src.routers.empresa import EmpresaRoutes
from src.routers.produtos import ProductRoutes

app = FastAPI()
app.include_router(colaboradorRoutes.router)
app.include_router(EmpresaRoutes.router)
app.include_router(ProductRoutes.router)


