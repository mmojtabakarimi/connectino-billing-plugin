from wazo_confd.helpers.validator import Validator, ValidationGroup


class RatingValidator(Validator):
    def validate(self, model):
        return


def build_rating_validator():
    rating_validator = RatingValidator()
    return ValidationGroup(create=[rating_validator], edit=[rating_validator])

# def build_queuefeature_validator():
#     queuefeature_validator = QueueFeatureValidator()
#     return ValidationGroup(create=[queuefeature_validator], edit=[queuefeature_validator])
