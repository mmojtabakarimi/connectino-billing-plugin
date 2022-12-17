from wazo_confd.helpers.validator import Validator, ValidationGroup


class RatingValidator(Validator):
    def validate(self, model):
        return


def build_rating_validator():
    rating_validator = RatingValidator()
    return ValidationGroup(create=[rating_validator], edit=[rating_validator])
