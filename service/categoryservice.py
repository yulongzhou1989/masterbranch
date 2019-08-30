from .meta import BaseService
from model import ArticleModel

class CategoryService(BaseService):

    def listCategoryWithCount(limit=BaseService.LIMIT):
        cats = BaseService.list(model_name='CategoryModel',limit=limit)
        for cat in cats['data']:
            cat_cnt = ArticleModel.scan(ArticleModel.category == cat['category_name'])
            list(cat_cnt)
            cat['cnt'] = cat_cnt.total_count
        return cats
