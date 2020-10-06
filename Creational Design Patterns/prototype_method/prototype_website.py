import copy


class Website:
    def __init__(self, name, domain, description, author, **kwargs):
        """Examples of optional attributes (kwargs)
        category, creation_date, technology, keywords
        """
        self.name = name
        self.domain = domain
        self.description = description
        self.author = author
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @property
    def __str__(self) -> str:
        summary = [f'Website: {self.name}.\n', ]
        info = vars(self).items()
        ordered_info = sorted(info)

        for attr, val in ordered_info:
            if attr == 'name':
                continue
            summary.append(f'{attr}: {val}\n')

        return ''.join(summary)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)

        if not found:
            raise ValueError(f'Incorrect object identifier: {identifier}')

        obj = copy.deepcopy(found)

        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj


def main():
    keywords = ('python', 'data', 'apis', 'automation')
    site1 = Website(name='ContentGardening',
                    domain="contentgardening.com",
                    description='Automation and data-driven apps',
                    author="Kamon Ayeva",
                    category='blog',
                    keywords=keywords)
    prototype = Prototype()
    identifier = 'prototype_v1'
    prototype.register(identifier, site1)
    site2 = prototype.clone(identifier, name='Content Gardening playground',
                            domain='play.contentgardening.com',
                            description='Experimentation for techniques featured on the blog',
                            category='Membership site',
                            creation_date='2020-10-05')

    print(f'{id(site1)} is {id(site2)}') if id(site1) is id(site2) else print(f'{id(site1)} is not {id(site2)}')


if __name__ == '__main__':
    main()
