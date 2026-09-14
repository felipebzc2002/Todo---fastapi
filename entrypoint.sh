#!/bin/sh


#===================================================
# EXECUTA AS MIGRAÇÔES DO BANCO DE DADOS
#===================================================
poetry run alembic upgrade head 

#===================================================
# INICIA A APLICAÇãO
#===================================================
poetry run uvicorn --host 0.0.0.0 --port 8000 fastapi_zero.app:app