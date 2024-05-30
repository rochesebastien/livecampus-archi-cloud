from typing import List, Optional, Union
from fastapi import FastAPI, HTTPException

from app.sql_client import SqlClient 

tags_metadata = [
    {
        "name": "Blog",
        "description": "Actions sur les blogs",
    },
    {
        "name": "Article",
        "description": "Actions sur les articles",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

client = SqlClient()

@app.get("/articles",
description="Récupère la liste des articles",
summary="Récupère la liste des articles",
tags=["Article"],
# response_model=List[Article]
)
def get_articles():
    return True

@app.get("/articles/{id}",
description="Récupère un article en fonction de l'id ",
summary="Récupère un article en fonction de l'id",
tags=["Article"],
# response_model=List[Article]
)
def get_article(id: int):
    return True

@app.post("/articles",
description="Ajoute un article",
summary="Ajoute un article",
tags=["Article"],
# response_model=List[Article]
)
def create_article():
    return True

@app.patch("/articles/{id}",
description="Modifie un article spécifique",
summary="Modifie un article spécifique",
tags=["Article"],
# response_model=List[Article]
)
def update_article(id: int):
    return True

@app.delete("/articles/{id}",
description="Supprime un article spécifique",
summary="Supprime un article spécifique",
tags=["Article"],
# response_model=List[Article]
)
def delete_article(id: int):
    return True

@app.get("/blogs",
description="Récupère la liste des blogs",
summary="Récupère la liste des blogs",
tags=["Blog"],
# response_model=List[Blog]
)
def get_blogs():
    return True

@app.get("/blogs/{id}",
description="Récupère un blog en fonction de l'id ",
summary="Récupère un article en fonction de l'id ",
tags=["Blog"],
# response_model=List[Blog]
)
def get_blog(id: int):
    return True

@app.post("/blogs",
description="Ajoute un blog",
summary="Ajoute un blog",
tags=["Blog"],
# response_model=List[Blog]
)
def create_blog():
    return True

@app.patch("/blogs/{id}",
description="Modifie un blog spécifique",
summary="Modifie un blog spécifique",
tags=["Blog"],
# response_model=List[Blog]
)
def update_blog(id: int):
    return True

@app.delete("/blogs/{id}",
description="Supprime un blog spécifique",
summary="Supprime un blog spécifique",
tags=["Blog"],
# response_model=List[Blog]
)
def delete_blog(id: int):
    return True