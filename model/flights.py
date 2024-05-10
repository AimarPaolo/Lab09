from dataclasses import dataclass
from datetime import datetime

@dataclass
class Flights:
    ID: int
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    DISTANCE: int
    CONTATORE: int

    def __hash__(self):
        return self.ID

    def __str__(self):
        return f"{self.ORIGIN_AIRPORT_ID} - {self.DESTINATION_AIRPORT_ID} - avg distance: {self.DISTANCE}"

    def __eq__(self, other):
        return self.ID == other.ID