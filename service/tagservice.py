from .meta import BaseService

class TagService(BaseService):

    def list(limit, last_evaluated_key=None):
        tags = BaseService.list(model_name='TagModel',limit=limit, last_evaluated_key=last_evaluated_key)
        tags['data'].sort(key=lambda x: x['tag_name'].upper())
        return tags
