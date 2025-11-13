import json
from urllib.parse import urljoin

import requests

from config.var_env import API_KEY_PRIM, BASE_URL_PRIM, PATH_GEOVELO, PATH_CALCULATEUR_IDFM
from src.itineraire.domain.ports.source_handler import SourceHandler

class ApiHandler(SourceHandler):
    def __init__(self):
        self.url_prim = urljoin(BASE_URL_PRIM, PATH_CALCULATEUR_IDFM)

        self.url_geovelo = urljoin(BASE_URL_PRIM, PATH_GEOVELO)

        self.headers = {'apiKey': API_KEY_PRIM}
        self.session = requests.Session()

        self.session.headers.update(self.headers)

    def get_address_coordinates(self, address_name: str) -> dict:
        params = {'q': address_name}
        r = self.session.get(f"{self.url_prim}/places", params=params)
        coordinates = r.json().get('places')[0].get('id').split(";")
        return {
            "longitude": float(coordinates[0]),
            "latitude": float(coordinates[1])
        }
    
    def get_itinerary(self, departure_coordinates: dict, arrival_coordinates: dict) -> dict:
        params = {
            'from': f"{departure_coordinates.get("longitude")};{departure_coordinates.get("latitude")}",
            'to': f"{arrival_coordinates.get("longitude")};{arrival_coordinates.get("latitude")}",
        }
        r = self.session.get(f"{self.url_prim}/journeys", params=params)
        return r.json()
    
    def get_itinerary_velo(
            self,
            departure_coordinates: dict,
            arrival_coordinates: dict,
            profile: str = "Default"
        ) -> list[dict]:
        body = {
            "waypoints": [
                {
                    "latitude": departure_coordinates.get("latitude"),
                    "longitude": departure_coordinates.get("longitude")
                },
                {
                    "latitude": arrival_coordinates.get("latitude"),
                    "longitude": arrival_coordinates.get("longitude")
                }
            ]
            ,
            "bikeDetails":{
                "profile": profile,
                "bikeType": "TRADITIONAL"
            }
        }
        r = self.session.post(f"{self.url_geovelo}/computedroutes", data=json.dumps(body))
        return r.json()