from .meta import BaseService
from model import WishModel
import queue as Q
from datetime import datetime

class WishService(BaseService):

    def updateStatus(wish_id, status):
        print(status)
        wish = WishModel(id=wish_id)
        try:
            wish.update(
                actions=[
                    WishModel.status.set(status),
                    WishModel.finish_time.set(str(datetime.now()) if status == 'off' else 'On Going')
                ],
                condition=(
                    (WishModel.id == wish_id)
                )
            )

        except Exception as e:
            print(str(e))
            return {'status' : 0}

        return {'status': 1}

    def listTopPriorityWishes(top=10, status='on'):
        dataItr = WishModel.scan(WishModel.status==status, limit=None, last_evaluated_key=None)
        data = []
        lek = None
        q = Q.PriorityQueue()
        for e in dataItr:
            lek = dataItr.last_evaluated_key
            e.real_time_cost = WishService.calDayDiff(e.create_time, e.finish_time)
            q.put(e)
            if (q.qsize() > int(top)):
                q.get()

        while not q.empty():
            data.append(q.get().to_dict())
        data.reverse()

        return {'data': data, 'lek': lek}

    def list(limit, last_evaluated_key=None):
        wishes = BaseService.list(model_name='WishModel',limit=limit, last_evaluated_key=last_evaluated_key)
        for wish in wishes['data']:
            wish['real_time_cost'] = WishService.calDayDiff(wish.get('create_time'), wish.get('finish_time'))
        return wishes

    def calDayDiff(create_time, finish_time):
        datetime_create = datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S.%f")
        datetime_finish = datetime.strptime(finish_time, "%Y-%m-%d %H:%M:%S.%f") if finish_time and finish_time != 'On Going' else datetime.now()
        days = int((datetime_finish - datetime_create).total_seconds() / (3600 * 24))
        if (days > 31):
            return str(int(days/31)) + ' Months'
        elif (days <= 31):
            return str(days)+ ' Days'
        else:
            return str(int(days/365)) + ' Years'
