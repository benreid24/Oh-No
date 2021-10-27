from typing import Any, Callable, Dict, List, Type

class EventListener:
    """
    A light wrapper over a map of Type -> Callable. This makes it easy to clean up a bunch of callbacks
    associated with a single object when its lifetime is over
    """

    def __init__(self):
        # type: () -> None
        self._handlers = {} # type: Dict[Type, Callable]

    def listen_for(self, event_type, callback):
        # type: (Type, Callable) -> None
        self._handlers[event_type] = callback

    def notify(self, event_type, event):
        # type: (Type, Any) -> None
        if event_type in self._handlers:
            self._handlers[event_type](event)

    def listens_to(self):
        # type: () -> List[Type]
        return list(self._handlers.keys())
