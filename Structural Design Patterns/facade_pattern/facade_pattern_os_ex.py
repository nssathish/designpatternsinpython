"""
    Facade Pattern
    --------------
    The pattern helps to hide the internal complexity of our system and
    expose only what is necessary to the client through a simplified interface.

    It is an abstraction layer implemented over an existing complex system.

    Use Case
    --------
    1. It provides a single, simple entry point to the complex system
        a. Achieved by encapsulation
    2. Client code remains unchanged while the application code is modified
    3. Pattern is useful when there are multiple layers in the application
        a. Client facing layer can have the facade interface
        b. The rest of the layers can communicate among themselves using
        other facade interfaces internally
"""
from enum import Enum
from abc import ABC, abstractmethod
from typing import Any

State = Enum('State', 'new running shutdown restart')


class Server(ABC):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self):
        pass


class FileServer(Server):

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def boot(self):
        print(f'File server started: {self}')

    def kill(self):
        print(f'File server killed: {self}')

    def create_file(self, username, permissions):
        print(f'{username} authenticated with {permissions}. Files can now be created.')


class ProcessServer(Server):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def boot(self):
        print(f'Process server: {self} started.')

    def kill(self):
        print(f'Process server: {self} killed.')

    def create_process(self, username, permissions):
        print(f'{username} authenticated with {permissions}. Processes can be spawned.')


class OperatingSystem:
    def __init__(self, name) -> None:
        self.state = State.new
        self.name = name
        self.fs = FileServer('OS file server')
        self.ps = ProcessServer('OS process server')

    def __str__(self):
        return self.name

    def start(self):
        print(f'{self} started...')
        self.state = State.running
        [xs.boot() for xs in (self.fs, self.ps)]

    def create_file(self, has_started):
        self.fs.create_file('sathish', 'rw--r--') if has_started == State.running else print(f'{self}OS has not yet '
                                                                                             f'started')

    def create_process(self, has_started):
        self.ps.create_process('sathish','CRUD') if has_started == State.running else print(f'{self}OS has not yet '
                                                                                            f'started')


def main():
    os_obj = OperatingSystem('satix')
    os_obj.start()
    os_obj.create_file(os_obj.state)
    os_obj.create_process(os_obj.state)


if __name__ == "__main__":
    main()