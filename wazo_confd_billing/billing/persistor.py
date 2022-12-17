from xivo_dao.helpers.persistor import BasePersistor
from xivo_dao.resources.utils.search import CriteriaBuilderMixin

from .model import RatingModel


class RatingPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = RatingModel

    def __init__(self, session, rating_search, tenant_uuids=None):
        self.session = session
        self.search_system = rating_search
        self.tenant_uuids = tenant_uuids

    def _find_query(self, criteria):
        query = self.session.query(RatingModel)
        # query = self._filter_tenant_uuid(query)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)

    def get_all_ratings(self, tenant_uuid):
        query = self.session.query(RatingModel)
        query = query.filter(RatingModel.tenant_uuid == tenant_uuid)
        return query
