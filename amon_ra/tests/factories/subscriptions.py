import factory.fuzzy


class SubscriptionKeysDictFactory(factory.DictFactory):
    p256dh = factory.Faker("md5")
    auth = factory.Faker("md5")


class SubscriptionDictFactory(factory.DictFactory):
    endpoint = factory.Faker("uri")
    expiration_time = None
    keys = factory.SubFactory(SubscriptionKeysDictFactory)
