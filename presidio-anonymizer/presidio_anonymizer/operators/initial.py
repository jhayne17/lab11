from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def operator_name(self) -> str:
        return self.__class__.__name__.lower()

    def operate(self, text: str, params: dict = None) -> str:
        if not text:
            return ""
        words = text.split()
        initials = [w[0].upper() + "." for w in words if w]
        return " ".join(initials)

    def validate(self, params: dict = None):
        return
