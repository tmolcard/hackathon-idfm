

from src.itineraire.domain.ports.source_handler import SourceHandler


class CalculItineraireVelo:
    def __init__(self, source_handler: SourceHandler):
        self.source_handler = source_handler

    def execute(self, departure_name: str, arrival_name: str) -> dict:
        departure_coordinates = self.source_handler.get_address_coordinates(address_name = departure_name)
        arrival_coordinates = self.source_handler.get_address_coordinates(address_name = arrival_name)

        itinerary = self.source_handler.get_itinerary_velo(departure_coordinates, arrival_coordinates)

        return itinerary
    

if __name__ == "__main__":
    from src.itineraire.infrastructure.api_handler import ApiHandler
    c = CalculItineraireVelo(ApiHandler())
    result = c.execute("32 rue Léopold Bellan", "34 avenue de l'Opéra")
    print(result)