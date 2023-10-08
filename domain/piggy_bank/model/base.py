from domain.domain_objects import EntityId


class PiggyBankId(EntityId):
    value: str

    def __eq__(self, other):
        return super().__eq__(other)

    def __hash__(self):
        return super().__hash__()
