from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import RatingModel

rating_config = SearchConfig(
    table=RatingModel,
    columns={
        'id': RatingModel.id,
        'tenant_uuid': RatingModel.tenant_uuid,
    },
    default_sort='id',
)


rating_search = SearchSystem(rating_config)
