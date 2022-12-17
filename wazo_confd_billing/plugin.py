import logging

from .billing.resource import RatingListResource, BillingItemResource, RaingItemResource
from .billing.services import build_rating_service
from wazo_call_logd_client import Client as CallLogdClient
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('Connectino billing plugin start loading')
        init_db(
            'postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-billing-plugin')
        api = dependencies['api']

        token_changed_subscribe = dependencies['token_changed_subscribe']
        call_logd_client = CallLogdClient(
            'localhost', verify_certificate=False)
        token_changed_subscribe(call_logd_client.set_token)

        rating_service = build_rating_service(call_logd_client)

        # Ratings
        api.add_resource(
            RatingListResource,
            '/ratings',
            endpoint='rating',
            resource_class_args=(rating_service,)
        )

        api.add_resource(
            RaingItemResource,
            '/ratings/<int:uuid>',

            resource_class_args=(rating_service,)
        )

        # Get all
        api.add_resource(
            BillingItemResource,
            '/billings/aparty/<aparty_number>',
            resource_class_args=(rating_service,)
        )

        logger.info('Connectino billing plugin loaded successfully')
