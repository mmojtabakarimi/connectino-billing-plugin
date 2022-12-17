from wazo_confd.helpers.resource import CRUDService

from . import dao

from .notifier import build_rating_notifier
from .validator import build_rating_validator


class RatingService(CRUDService):
    def __init__(self, call_logd_client, dao, validator, notifier):
        self.call_logd_client = call_logd_client
        self.dao = dao
        self.validator = validator
        self.notifier = notifier

    def get_all_ratings(self, tenant_uuid):
        return self.dao.get_all_ratings(tenant_uuid)

    def get_all_billing_by_aparty_number(self, tenant_uuid, aparty_number, from_date, until_date):

        self.call_logd_client.tenant_uuid = tenant_uuid
        cdr_records = self.call_logd_client.cdr.list(limit=20)
        return cdr_records

    def calculate_rating(self, bulk, ratings):
        rated_cdr = []
        for key1, value1 in bulk.items():
            if key1 == 'items':
                for cdr in value1:
                    for key, value in cdr.items():
                        if (key == 'answered'):
                            if (value == True):
                                rate = self.find_rate(
                                    ratings, cdr['destination_line_identity'], cdr['duration'], cdr['call_type'])
                                cdr['rate'] = rate
                                rated_cdr.append(cdr)
        return rated_cdr

    def find_rate(self, ratings, provider_name, duration, call_type):
        data = ratings['items']
        cost = '1'
        for rating in data:
            for key, value in rating.items():
                if (key == 'provider_name'):
                    if (value == provider_name):
                        if int(call_type) == 1:
                            cost = str((-(-int(duration)//60))
                                       * int(rating['local']))
                        if int(call_type) == 2:
                            cost = str((-(-int(duration)//60))
                                       * int(rating['national']))
                        if int(call_type) == 3:
                            cost = str((-(-int(duration)//60))
                                       * int(rating['mobile']))
                        if int(call_type) == 4:
                            cost = str((-(-int(duration)//60)) *
                                       int(rating['international']))
        return cost


def build_rating_service(call_logd_client):
    return RatingService(call_logd_client, dao, build_rating_validator(), build_rating_notifier())
