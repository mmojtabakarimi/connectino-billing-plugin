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

    # def get_all_survey_by_queue_id(self, tenant_uuid, queue_id):
    #     query = self.session.query(SurveyModel)
    #     query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
    #     query = query.filter(SurveyModel.queue_id == queue_id)
    #     return query
#     def get_average_survey_by_queue_id(self, tenant_uuid, queue_id, from_date, until_date):
#         query = self.session.query(SurveyModel)
#         query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
#         query = query.filter(SurveyModel.queue_id == queue_id)
#         query = query.filter(SurveyModel.timestamp > from_date)
#         query = query.filter(SurveyModel.timestamp < until_date)
#
#         return query
#
#     def get_average_survey_by_agent_id(self, tenant_uuid, agent_id, from_date, until_date):
#         query = self.session.query(SurveyModel)
#         query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
#         query = query.filter(SurveyModel.agent_id == agent_id)
#         query = query.filter(SurveyModel.timestamp > from_date)
#         query = query.filter(SurveyModel.timestamp < until_date)
#         return query
#
#     def get_average_survey_all_agent(self, tenant_uuid, from_date, until_date):
#         query = self.session.query(SurveyModel)
#         query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
#         query = query.filter(SurveyModel.timestamp > from_date)
#         query = query.filter(SurveyModel.timestamp < until_date)
#         return query
#
#     def get_average_survey_all_queue(self, tenant_uuid, from_date, until_date):
#         query = self.session.query(SurveyModel)
#         query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
#         query = query.filter(SurveyModel.timestamp > from_date)
#         query = query.filter(SurveyModel.timestamp < until_date)
#         return query
#
#     def get_average_survey_agent_queue(self, tenant_uuid, queue_id, agent_id, from_date, until_date):
#         query = self.session.query(SurveyModel)
#         query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
#         query = query.filter(SurveyModel.agent_id == agent_id)
#         query = query.filter(SurveyModel.queue_id == queue_id)
#         query = query.filter(SurveyModel.timestamp > from_date)
#         query = query.filter(SurveyModel.timestamp < until_date)
#         return query
#
#
# class QueueFeatursPersistor(CriteriaBuilderMixin, BasePersistor):
#     _search_table = QueueFeaturesModel
#
#     def __init__(self, session, queuefeature_search, tenant_uuids=None):
#         self.session = session
#         self.search_system = queuefeature_search
#         self.tenant_uuids = tenant_uuids
#
#     def get_all_queue_features(self, tenant_uuid):
#         query = self.session.query(QueueFeaturesModel)
#         query = query.filter(QueueFeaturesModel.tenant_uuid == tenant_uuid)
#         return query
#
#     def _find_query(self, criteria):
#         query = self.session.query(QueueFeaturesModel)
#         # query = self._filter_tenant_uuid(query)
#         return self.build_criteria(query, criteria)
#
#     def _search_query(self):
#         return self.session.query(self.search_system.config.table)
