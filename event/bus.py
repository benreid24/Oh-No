from typing import Any, Type, Dict, List
from collections import defaultdict

from .listener import EventListener


class EventBus:
    def __init__(self):
        # type: () -> None
        self._listeners = defaultdict(list) # type: Dict[Type, List[EventListener]]
        self._listener_map = defaultdict(list) # type: Dict[EventListener, List[Type]]

    def subscribe(self, listener):
        # type: (EventListener) -> None
        ts = listener.listens_to()
        self._listener_map[listener] = ts
        for t in ts:
            self._listeners[t].append(listener)

    def push(self, event_type, event):
        # type: (Type, Any) -> None
        if event_type in self._listeners:
            for l in self._listeners[event_type]:
                l.notify(event_type, event)
