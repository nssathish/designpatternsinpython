"""
Adapter Pattern
---------------
Structural design pattern that helps make incompatible interfaces, compatible.
If we have an old component and we want to use it in our new system (or)
a new component to use it in our old system and the two can rarely communicate
without require code changes
1. An extra layer to between the (old component and new system ) or (new component
and old system) which will make all the required modifications

Use-cases
---------
1. One of the two incompatible interfaces is either
    a.Foreign - if it is foreign it means we have no access to it
    b.Legacy - if it is old then it is usually impractical to refactor it

Adapter will help to make things work here because
a. it does not require access to the source code of the foreign interface.
b. It is also often a pragmatic solution if we have to reuse some legacy code
"""


class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the club {self.name}'

    def organize_event(self):
        return 'hires an artist to perform for the people'


class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the musician {self.name}'

    def play(self):
        return 'plays music'


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the dancer {self.name}'

    def dance(self):
        return 'does a dance performance'


class Adapter:
    def __init__(self, obj, adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Club('Jazz cafe'), Musician('Roy Ayers'), Dancer('Shane Sparks')]
    for obj in objects:
        if hasattr(obj, 'play') or hasattr(obj, 'dance'):
            if hasattr(obj, 'play'):
                adapted_methods = dict(organize_event=obj.play)
            elif hasattr(obj, 'dance'):
                adapted_methods = dict(organize_event=obj.dance)
            else:
                adapted_methods = dict()
            # referencing the adapted object here
            obj = Adapter(obj, adapted_methods)
        print(f'{obj} {obj.organize_event()}')


if __name__ == "__main__":
    main()
