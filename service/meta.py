import model

class BaseService(object):

    LIMIT = 10

    def list(model_name, last_evaluated_key=None, limit=LIMIT):
        dataItr = getattr(model, model_name).scan(limit=limit, last_evaluated_key=last_evaluated_key)
        data = []
        for e in dataItr:
            lek = dataItr.last_evaluated_key
            data.append(e.to_dict())

        return {'data': data, 'lek': lek}

    def getByHashKey(model_name, hash_key):
        dataItr = getattr(model, model_name).query(hash_key)
        dataObj = dataItr.next()
        if (dataObj == None):
            return None
        else:
            return dataObj.to_dict()
