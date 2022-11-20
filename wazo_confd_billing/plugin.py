import logging

from .billing.resource import RatingListResource
from .billing.services import build_rating_service
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('Connectino billing plugin start loading')
        init_db(
            'postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-billing-plugin')
        api = dependencies['api']
        rating_service = build_rating_service()
        #queuefeature_service = build_queuefeature_service()

        # Get all Ratings
        api.add_resource(
            RatingListResource,
            '/ratings',
            endpoint='rating',
            resource_class_args=(rating_service,)
        )

#         # Get all survey by agent_id
#         api.add_resource(
#             SurveyAgentItemResource,
#             '/surveys/agent/<agent_id>',
#             resource_class_args=(survey_service,)
#         )
#
#         # Get all survey b queue_id
#         api.add_resource(
#             SurveyQueueItemResource,
#             '/surveys/queue/<queue_id>',
#             resource_class_args=(survey_service,)
#         )
#
#         # Get average survey rating by  queue_id
#         api.add_resource(
#             SurveyQueueAverageItemResource,
#             '/surveys/average/queue/<queue_id>',
#             resource_class_args=(survey_service,)
#         )
#
#         # Get average survey rating by agent_id
#         api.add_resource(
#             SurveyAgentAverageItemResource,
#             '/surveys/average/agent/<agent_id>',
#             resource_class_args=(survey_service,)
#         )
#
#         # Get average survey rating for queue_id at specific agent_id
#         api.add_resource(
#             SurveyAgentInQueueAverageItemResource,
#             '/surveys/average/queue/<queue_id>/agent/<agent_id>',
#             resource_class_args=(survey_service,)
#         )
#
#         # Get average survey rating for all agent
#         api.add_resource(
#             SurveyAllAgentAverageItemResource,
#             '/surveys/average/allagent',
#             resource_class_args=(survey_service,)
#         )
#         # Get average survey rating for all queue
#         api.add_resource(
#             SurveyAllQueueAverageItemResource,
#             '/surveys/average/allqueue',
#             resource_class_args=(survey_service,)
#         )
#
#         # Get All queue-features
#         api.add_resource(
#             QueueFeaturesListResource,
#             '/queue-features',
#             endpoint='queuefeatures',
#             resource_class_args=(queuefeature_service,)
#         )
#
#         # Add(post)/Edit(put) new queue-features
#         api.add_resource(
#             QueueFeaturesItemResource,
#             '/queue-features/<int:uuid>',
#             resource_class_args=(queuefeature_service,)
#         )

        logger.info('Connectino billing plugin loaded successfully')