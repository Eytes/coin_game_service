from .mongo.async_mongo_helper import mongo_helper
from .mongo.mongo_registry import AsyncMongoRegistryFactory

mongo_registry_factory = AsyncMongoRegistryFactory(mongo_helper.get_database())
CoinMongoRegistry = mongo_registry_factory.get_registry("coins")
