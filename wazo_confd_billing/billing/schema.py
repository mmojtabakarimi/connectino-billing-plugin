from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema

class RatingSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    tenant_uuid = fields.String(dump_only=True)
    source_number = fields.String(dump_only=True)
    destination_number = fields.String(dump_only=True)
    rate_per_sec = fields.String(dump_only=True)
    rate_per_min = fields.String(dump_only=True)
    call_type = fields.String(dump_only=False)
    cost = fields.String(dump_only=False)
    currency = fields.String(dump_only=False)
    free = fields.String(dump_only=False)
    timestamp = fields.String(dump_only=True)
    reserved = fields.String(dump_only=True)


