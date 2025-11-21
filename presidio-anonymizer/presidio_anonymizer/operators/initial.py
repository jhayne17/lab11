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
        initials_list = []

        for word in words:
            # Find index of first alphanumeric character
            for i, char in enumerate(word):
                if char.isalnum():
                    # Preserve prefix
                    prefix = word[:i]
                    initial = char.upper() if char.isalpha() else char
                    initials_list.append(f"{prefix}{initial}.")
                    break
            else:
                # No alphanumeric character in word
                initials_list.append(word)

        return " ".join(initials_list)

    def validate(self, params: dict = None):
        return
