from xivo_dao.helpers.db_manager import daosession
from .persistor import RatingPersistor
from .search import rating_search

from datetime import timedelta


@daosession
def _ratingPersistor(session, tenant_uuids=None):
    return RatingPersistor(session, rating_search, tenant_uuids)


def get_all_ratins(tenant_uuid):
    return _ratingPersistor().get_all_ratings(tenant_uuid)


def search(tenant_uuids=None, **parameters):
    return _ratingPersistor(tenant_uuids).search(parameters)


def get_by(tenant_uuids=None, **criteria):
    return _ratingPersistor(tenant_uuids).get_by(criteria)

#
#
# def get_all_survey_by_queue_id(tenant_uuid, queue_id):
#     return _persistor().get_all_survey_by_queue_id(tenant_uuid, queue_id)
#
#
# def get_all_survey_by_agent_id(tenant_uuid, agent_id):
#     return _persistor().get_all_survey_by_agent_id(tenant_uuid, agent_id)
#
#
# def get_average_survey_by_queue_id(tenant_uuid, queue_id, from_date, until_date):
#     return _persistor().get_average_survey_by_queue_id(tenant_uuid, queue_id, from_date, until_date)
#
#
# def get_average_survey_by_agent_id(tenant_uuid, agent_id, from_date, until_date):
#     return _persistor().get_average_survey_by_agent_id(tenant_uuid, agent_id, from_date, until_date)
#
#
# def get_average_survey_all_agent(tenant_uuid, from_date, until_date):
#     return _persistor().get_average_survey_all_agent(tenant_uuid, from_date, until_date)
#
#
# def get_average_survey_all_queue(tenant_uuid, from_date, until_date):
#     return _persistor().get_average_survey_all_queue(tenant_uuid, from_date, until_date)
#
#
# def get_average_survey_agent_queue(tenant_uuid, queue_id, agent_id, from_date, until_date):
#     return _persistor().get_average_survey_agent_queue(tenant_uuid, queue_id, agent_id, from_date, until_date)
