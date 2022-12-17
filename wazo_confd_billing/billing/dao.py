from xivo_dao.helpers.db_manager import daosession
from .persistor import RatingPersistor
from .search import rating_search


@daosession
def _ratingPersistor(session, tenant_uuids=None):
    return RatingPersistor(session, rating_search, tenant_uuids)


def get_all_ratins(tenant_uuid):
    return _ratingPersistor().get_all_ratings(tenant_uuid)


def create(rating):
    return _ratingPersistor().create(rating)


def search(tenant_uuids=None, **parameters):
    return _ratingPersistor(tenant_uuids).search(parameters)


def get_by(tenant_uuids=None, **criteria):
    return _ratingPersistor(tenant_uuids).get_by(criteria)


def get(rating_uuid, tenant_uuids=None):
    return _ratingPersistor(tenant_uuids).get_by({'id': rating_uuid})


def delete(rating):
    _ratingPersistor().delete(rating)


def put(rating):
    _ratingPersistor().put(rating)


def edit(sample):
    _ratingPersistor().edit(sample)
