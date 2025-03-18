from collections import deque
import time
from Wikipedia import get_wiki_links
from EnEx_API import *

def bidirectional_bfs_wikipedia(start, goal):
    """
    Finds the shortest path between two Wikipedia pages using bidirectional BFS.
    :param start: The start Wikipedia page title.
    :param goal: The target Wikipedia page title.
    :return: The shortest path as a list of page titles.
    """
    if start == goal:
        return [start]

    forward_queue = deque([(start, [start])])
    backward_queue = deque([(goal, [goal])])

    forward_visited = {start: [start]}
    backward_visited = {goal: [goal]}

    while forward_queue and backward_queue:
        # Expand the smaller queue for efficiency
        if len(forward_queue) <= len(backward_queue):
            result = expand_queue_wikipedia(forward_queue, forward_visited, backward_visited, direction="forward")
        else:
            result = expand_queue_wikipedia(backward_queue, backward_visited, forward_visited, direction="backward")

        if result:
            return result  # Return the shortest path when found

    return None  # No path found

def expand_queue_wikipedia(queue, visited, other_visited, direction):
    """
    Expands the search queue by fetching Wikipedia objects and checking their links.
    :param queue: The queue to expand.
    :param visited: The visited dictionary for this direction.
    :param other_visited: The visited dictionary of the opposite direction.
    :param direction: "forward" for outgoing links, "backward" for ingoing links.
    :return: The shortest path if found, otherwise None.
    """
    for _ in range(len(queue)):  # Expand all nodes at the current depth
        current, path = queue.popleft()
        wiki_page = get_wiki_links(current)  # Fetch Wikipedia object
        
        neighbors = wiki_page.outgoinglinks if direction == "forward" else wiki_page.ingoinglinks

        for neighbor in neighbors:
            if neighbor in visited:  # Skip already visited nodes in this direction
                continue

            new_path = path + [neighbor] if direction == "forward" else [neighbor] + path
            visited[neighbor] = new_path

            if neighbor in other_visited:  # Meeting point found!
                return merge_paths(new_path, other_visited[neighbor])

            queue.append((neighbor, new_path))

        time.sleep(0.5)  # Prevent excessive API calls

    return None

def merge_paths(path1, path2):
    """ Merges two paths from forward and backward search. """
    return path1 + path2[1:]


