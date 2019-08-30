from .meta import BaseService
from model import ArticleModel

class ArticleService(BaseService):

    def searchArticleByCat(cat, limit=None, last_evaluated_key=None):
        dataItr = ArticleModel.scan(ArticleModel.category==cat, limit=limit, last_evaluated_key=last_evaluated_key)
        data = []
        lek = None
        for e in dataItr:
            lek = dataItr.last_evaluated_key
            data.append(e.to_dict())

        return {'data': data, 'lek': lek}

    def searchArticleByTag(tag, limit=None, last_evaluated_key=None):
        dataItr = ArticleModel.scan(ArticleModel.tags.contains(tag), limit=limit, last_evaluated_key=last_evaluated_key)
        data = []
        lek = None
        for e in dataItr:
            lek = dataItr.last_evaluated_key
            data.append(e.to_dict())

        return {'data': data, 'lek': lek}

    def searchArticleByKeyword(keyword, limit=None, last_evaluated_key=None):
        dataItr = ArticleModel.scan(ArticleModel.category.startswith(keyword) | ArticleModel.title.contains(keyword) | ArticleModel.content.contains(keyword), limit=limit, last_evaluated_key=last_evaluated_key)
        data = []
        lek = None
        for e in dataItr:
            lek = dataItr.last_evaluated_key
            data.append(e.to_dict())

        return {'data': data, 'lek': lek}
