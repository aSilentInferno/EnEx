from collections import deque
import time
from wikipedia import Wikipedia
from EnEx_API import get_wiki_links

def bidirectional_bfs_wikipedia(start, goal):
    """
    Findet den kürzesten Pfad zwischen zwei Wikipedia-Seiten mittels bidirektionalem Breitensuche. (BFS)
    auswahl des Suchalgorithmus basierend auf den fünden aus https://www2.informatik.uni-stuttgart.de/bibliothek/ftp/medoc.ustuttgart_fi/DIP-3410/DIP-3410.pdf
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
        # Die kleine Anzahl von Schritten wird zuerst durchgeführt, um die Anzahl der Schritte zu minimieren
        if len(forward_queue) <= len(backward_queue):
            result = expand_queue_wikipedia(forward_queue, forward_visited, backward_visited, direction="forward")
        else:
            result = expand_queue_wikipedia(backward_queue, backward_visited, forward_visited, direction="backward")

        if result:
            return result

    return None

def expand_queue_wikipedia(queue, visited, other_visited, direction):
    """
    Erweitert die Suchwarteschlange, indem Wikipedia-Objekte abgerufen und deren Links überprüft werden.
    :param queue: Die Warteschlange, die erweitert werden soll.
    :param visited: Das besuchte Dictionary für diese Richtung.
    :param other_visited: Das besuchte Dictionary der entgegengesetzten Richtung.
    :param direction: "forward" für ausgehende Links, "backward" für eingehende Links.
    :return: Der kürzeste Pfad, wenn gefunden, andernfalls None.
    """
    for _ in range(len(queue)):
        current, path = queue.popleft()
        wiki_page = get_wiki_links(current)
        
        neighbors = wiki_page.ausgehende_links if direction == "forward" else wiki_page.eingehende_links

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            new_path = path + [neighbor] if direction == "forward" else [neighbor] + path
            visited[neighbor] = new_path

            if neighbor in other_visited:  # Wenn Seiten in beiden Richtungen gefunden wurden, gibt es eine Lösung
                return merge_paths(new_path, other_visited[neighbor],direction)

            queue.append((neighbor, new_path))

        time.sleep(0.5)  # Verhindere Unnötige Anfragen an die Wikipedia-API

    return None

def merge_paths(erweiterter_pfad, umgekehrter_pfad, direction):
    """ Fügt die Beiden Pfade zusammen. """
    # path1 is erweiterter Pfad, path2 ist der Pfad der anderen Richtung
    if direction == "forward":
        return erweiterter_pfad + umgekehrter_pfad[1:]
    else:
        return umgekehrter_pfad + erweiterter_pfad[1:]