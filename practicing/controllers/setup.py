from resources.category import Category, CategoryList
from .category import CategoryController
from .auth import AuthController 

def Controller(app, api):
    AuthController(app, api)
    CategoryController(api)
    pass
