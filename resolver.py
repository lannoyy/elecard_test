from circle import Circle
from typing import List


class Resolver:

    def find_right_side(self, circles: List[Circle]):
        return max(
            [i.right_border for i in circles]
        )

    def find_left_side(self, circles: List[Circle]):
        return min(
            [i.left_border for i in circles]
        )

    def find_upper_side(self, circles: List[Circle]):
        return max(
            [i.upper_border for i in circles]
        )

    def find_lower_side(self, circles: List[Circle]):
        return min(
            [i.lower_border for i in circles]
        )

    def resolve(self, circles: List[Circle]) -> dict:
        """Get coordinates for result"""
        return ({
            "right_top": {
                "x": self.find_right_side(circles),
                "y": self.find_upper_side(circles),
            },
            "left_bottom": {
                "x": self.find_left_side(circles),
                "y": self.find_lower_side(circles)
            }
        })
