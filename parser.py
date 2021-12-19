from typing import List
from circle import Circle


class Parser:

    def create_circles(self, json_response: List[List[dict]]) -> List[List[Circle]]:
        """Create circles from Elecard API response"""
        all_circles = []
        for circles_set in json_response:
            temp_circles_set = []
            for circle in circles_set:
                temp_circles_set.append(
                    Circle(
                        x=circle['x'],
                        y=circle['y'],
                        r=circle['radius'],
                    )
                )
            all_circles.append(temp_circles_set)
        return all_circles
