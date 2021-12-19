from circle import Circle
from resolver import Resolver
from requester import Requester
from parser import Parser


if __name__ == '__main__':
    circles = Parser().create_circles(json_response=Requester().get_tasks())
    results = [Resolver().resolve(circle_set) for circle_set in circles]
    print(Requester().send_results(results))
