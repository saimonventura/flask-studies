from resources.category import Category, CategoryList


def CategoryController(api):
    api.add_resource(Category, '/category/<string:name>')
    api.add_resource(CategoryList, '/category')
    pass
