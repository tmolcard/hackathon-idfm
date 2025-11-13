from abc import ABC, abstractmethod


class SourceHandler(ABC):
    @abstractmethod
    def get_itinerary(self, departure_coordinates: dict, arrival_coordinates: dict) -> dict:
        pass

    @abstractmethod
    def get_address_coordinates(self, address_name: str) -> dict:
        pass

    @abstractmethod
    def get_itinerary_velo(
        self,
        departure_coordinates: dict,
        arrival_coordinates: dict,
        profile: str = "Default"
    ) -> list[dict]:
        pass
