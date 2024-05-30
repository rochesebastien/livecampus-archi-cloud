from typing import List, Optional, Union
from fastapi import FastAPI, HTTPException

from app.sql_client import SqlClient 
from app.schemas.blog import Blog, BlogCreate
from app.schemas.article import Article, ArticleCreate

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
sql_client = SqlClient()

@app.get("/articles",
description="Récupère la liste des articles",
summary="Récupère la liste des articles",
tags=["Article"],
response_model=List[Article]
)
def get_articles():
    return sql_client.get_articles()

@app.get("/articles/{article_id}",
description="Récupère un article en fonction de l'id ",
summary="Récupère un article en fonction de l'id",
tags=["Article"],
response_model=Article
)
def get_article(article_id: int):
    return sql_client.get_article(article_id)

@app.post("/articles",
description="Ajoute un article",
summary="Ajoute un article",
tags=["Article"],
response_model=Article
)
def create_article(article: ArticleCreate):
    return sql_client.create_article(article)

@app.patch("/articles/{article_id}",
description="Modifie un article spécifique",
summary="Modifie un article spécifique",
tags=["Article"],
response_model=Article
)
def update_article(article_id: int):
    return sql_client.update_article(article_id)

@app.delete("/articles/{article_id}",
description="Supprime un article spécifique",
summary="Supprime un article spécifique",
tags=["Article"],
)
def delete_article(article_id: int):
    return sql_client.delete_article(article_id)

@app.get("/blogs",
description="Récupère la liste des blogs",
summary="Récupère la liste des blogs",
tags=["Blog"],
response_model=List[Blog]
)
def get_blogs():
    blogs = sql_client.get_blogs()
    return blogs 

@app.get("/blogs/{blog_id}",
description="Récupère un blog en fonction de l'id ",
summary="Récupère un article en fonction de l'id ",
tags=["Blog"],
response_model=Blog
)
def get_blog(blog_id: int):
    return sql_client.get_blog(blog_id)

@app.post("/blogs",
description="Ajoute un blog",
summary="Ajoute un blog",
tags=["Blog"],
response_model=Blog
)
def create_blog(blog: BlogCreate):
    return sql_client.create_blog(blog)

@app.patch("/blogs/{id}",
description="Modifie un blog spécifique",
summary="Modifie un blog spécifique",
tags=["Blog"],
response_model=Blog
)
def update_blog(blog_id: int):
    return sql_client.update_blog(blog_id)

@app.delete("/blogs/{id}",
description="Supprime un blog spécifique",
summary="Supprime un blog spécifique",
tags=["Blog"],
)
def delete_blog(id: int):
    return sql_client.delete_blog(id)