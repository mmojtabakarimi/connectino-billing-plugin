from wazo_confd.helpers.validator import Validator, ValidationGroup


class BillingValidator(Validator):
    def validate(self, model):
        return


def build_rating_validator():
    def validate(self, model):
        return

# def build_queuefeature_validator():
#     queuefeature_validator = QueueFeatureValidator()
#     return ValidationGroup(create=[queuefeature_validator], edit=[queuefeature_validator])
