from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_rating_notifier
from .validator import build_rating_validator


class RatingService(CRUDService):
    def get_all_ratings(self, tenant_uuid):
        return dao.get_all_ratings(tenant_uuid)
