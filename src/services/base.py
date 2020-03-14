"""
Handles shared business logic for services that are directly bind with a repository.
e.g. PersonService
For data retrieval/modification/deletion from DB; it relies on repository layer.
"""


class BaseService(object):
    def __init__(self, repository=None):
        """
        Initializes the Service object
        :param repository: e.g. PersonRepository
        It is nullable as there can be a service which is not bind to any service.
        """
        if repository is not None:
            self.repository = repository()

    def get(self, entity_id):
        entity = self.repository.get(entity_id)
        if not entity:
            raise Exception('No Record Found.')
        return entity

    def get_all(self):
        entities = self.repository.get_all()
        return entities

    def delete(self, entity_id):
        entity = self.get(entity_id)
        if not entity:
            raise Exception('No Record Found.')
        self.repository.delete(entity)

    def update(self, entity):
        self.repository.update(entity)
        return entity

    def create(self, entity):
        self.repository.create(entity)
        entity = self.repository.get(entity.id)
        return entity
