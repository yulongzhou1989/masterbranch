from .meta import BaseService
from model import ArticleModel

class CategoryService(BaseService):

    def listCategoryWithCount(limit=BaseService.LIMIT):
        cats = BaseService.list(model_name='CategoryModel',limit=limit)
        for cat in cats['data']:
            print(cat)
            cat_cnt = ArticleModel.count('id', ArticleModel.category == cat['category_name'])
            cat['cnt'] = cat_cnt
        print(cats['data'])
        return cats
