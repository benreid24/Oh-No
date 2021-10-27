from typing import Any, List, Tuple

from pygame.draw import rect as draw_rect, circle as draw_circle
from camera import Camera
from component.circle_graphic import CircleGraphic
from component.orbital_physics import OrbitalPhysics
from component.physics import Physics
from component.position import Position, Vector

from constants import LIGHT_ORANGE, MINIMAP_BACKGROUND, MINIMAP_SIZE, SOLAR_SYSTEM_SIZE
from event.bus import EventBus
from event.listener import EventListener
from event.events.entity_spawn import EntitySpawnEvent
from entity.entity import Entity
from component.graphics import Graphics
from component.minimap import ShowsOnMinimap

DEFAULT_SIZE_SCALE = 13 / 425


class Minimap:
    def __init__(self, event_bus):
        # type: (EventBus) -> None
        self._listener = EventListener()
        self._listener.listen_for(EntitySpawnEvent, self._handle_spawn)
        event_bus.subscribe(self._listener)

        self._entities = [] # type: List[Entity]
        self._camera = Camera(
            size=Vector(SOLAR_SYSTEM_SIZE * 0.7, SOLAR_SYSTEM_SIZE * 0.7),
            render_region=(0, 0, MINIMAP_SIZE[0], MINIMAP_SIZE[1]),
            minimap=True
        )
        self._camera.position.x = -self._camera.size.x / 2
        self._camera.position.y = -self._camera.size.y / 2
        self._camera.set_entity_scale(Vector(DEFAULT_SIZE_SCALE, DEFAULT_SIZE_SCALE))

    def _handle_spawn(self, event):
        # type: (EntitySpawnEvent) -> None
        if Graphics in event.entity.components and ShowsOnMinimap in event.entity.components:
            self._entities.append(event.entity)

    def render(self, surface, area):
        # type: (Any, Tuple[int, int, int, int]) -> None
        self._camera.set_render_region(area)
        self._camera.set_entity_scale(Vector(DEFAULT_SIZE_SCALE, DEFAULT_SIZE_SCALE))

        dummy = Entity(Position(0, 0), Graphics())
        circle = CircleGraphic(LIGHT_ORANGE, 1, 1)

        draw_rect(surface, MINIMAP_BACKGROUND, area)
        for entity in self._entities:
            if entity.components[ShowsOnMinimap].render_override:
                entity.components[ShowsOnMinimap].render_override.render(surface, self._camera, entity)
            else:    
                entity.components[Graphics].render(surface, self._camera, entity)
            
            if Physics in entity.components:
                p: Physics = entity.components[Physics]
                if isinstance(p, OrbitalPhysics):
                    draw_circle(
                        surface,
                        LIGHT_ORANGE,
                        self._camera.transform_point(p.parent.position),
                        self._camera.transform_global_scalar(p.radius),
                        width=1
                    )
