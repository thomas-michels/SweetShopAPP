import flet as ft
from abc import ABC
from enum import Enum

class OrderStatusEnum(str, Enum):
    PENDING = "PENDING"
    IN_PREPARATION = "IN_PREPARATION"
    DONE = "DONE"


class OrderStatus(ABC):

    def __init__(self, label: str, color: str) -> None:
        self.label = label
        self.color = color


class PendingStatus(OrderStatus):

    def __init__(self) -> None:
        label = "Pendente"
        color = ft.colors.RED_600
        super().__init__(label, color)


class InPreparationStatus(OrderStatus):

    def __init__(self) -> None:
        label = "Em preparação"
        color = ft.colors.ORANGE_300
        super().__init__(label, color)


class DoneStatus(OrderStatus):

    def __init__(self) -> None:
        label = "Concluído"
        color = ft.colors.GREEN_600
        super().__init__(label, color)
