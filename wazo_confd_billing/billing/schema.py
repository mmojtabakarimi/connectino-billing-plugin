from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class RatingSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    tenant_uuid = fields.String(dump_only=True)
    provider_name = fields.String(dump_only=False)
    local = fields.String(dump_only=False)
    national = fields.String(dump_only=False)
    mobile = fields.String(dump_only=False)
    international = fields.String(dump_only=False)
    currency = fields.String(dump_only=False)
    free = fields.String(dump_only=False)
