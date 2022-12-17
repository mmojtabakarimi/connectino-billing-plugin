import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import RatingModel
from .schema import RatingSchema

logger = logging.getLogger(__name__)


class RatingListResource(ListResource):
    schema = RatingSchema
    model = RatingModel

    def build_headers(self, model):
        return {'Location': url_for('rating', uuid=model.id, _external=True)}

    @required_acl('confd.rating.read')
    def get(self):
        return super().get()

    @required_acl('confd.rating.create')
    def post(self):
        return super().post()


class RaingItemResource(ItemResource):
    schema = RatingSchema
    model = RatingModel

    @required_acl('confd.ratings.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.ratings.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.ratings.delete')
    def delete(self, uuid):
        return super().delete(uuid)


class BillingItemResource(ListResource):
    schema = RatingSchema
    model = RatingModel

    def build_headers(self, model):
        return {'Location': url_for('rating', uuid=model.id, _external=True)}

    @required_acl('confd.rating.read')
    def get(self, aparty_number):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_date = request.args.get('start')
        until_date = request.args.get('end')
        bulk = self.service.get_all_billing_by_aparty_number(
            tenant_uuid, aparty_number, from_date, until_date)
        ratings = super().get()

        rated_cdr = self.service.calculate_rating(bulk, ratings)
        return {'total': '1', 'items': rated_cdr}

    @required_acl('confd.rating.create')
    def post(self):
        return super().post()
