from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.category import CategoryModel


class Category(Resource):
    def get(self, name):
        category = CategoryModel.find_by_name(name)
        if category:
            return category.json()
        return {'message': 'Category not found'}, 404

    @jwt_required()
    def post(self, name):
        if CategoryModel.find_by_name(name):
            return {'message': "An category with name '{}' already exists.".format(name)}, 400

        category = CategoryModel(name)

        try:
            category.save_to_db()
        except:
            return {"message": "An error occurred inserting the category."}, 500

        return category.json(), 201

    @jwt_required()
    def delete(self, name):
        category = CategoryModel.find_by_name(name)
        if category:
            category.delete_from_db()
            return {'message': 'Category deleted.'}
        return {'message': 'Category not found.'}, 404


class CategoryList(Resource):
    def get(self):
        return {'categories': [category.json() for category in CategoryModel.query.all()]}
