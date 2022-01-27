import rubik


def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    # initialize
    current_f = set([start])
    parent_f = dict()
    current_b = set([end])
    parent_b = dict()

    # diameter: 14
    for i in range(16):  # go two more levels
        intersection = check_intersection(
            current_f, current_b, parent_f, parent_b, start, end)
        if intersection is not None:
            return intersection

        if i % 2 == 0:
            # forward BFS
            current_f = single_level_bfs(current_f, parent_f)
        else:
            # backward BFS
            current_b = single_level_bfs(current_b, parent_b)

    return None


def get_next_neighbors(pos):
    return [(rubik.perm_apply(twist, pos), twist) for twist in rubik.quarter_twists]


def single_level_bfs(current, parent):
    next = []
    for pos in current:
        for next_pos, twist in get_next_neighbors(pos):
            if next_pos not in parent:
                parent[next_pos] = (pos, twist)
                next.append(next_pos)
    return set(next)


def check_intersection(current_f, current_b, parent_f, parent_b, start, end):
    intersection = current_f & current_b
    if intersection:
        intersect_point = intersection.pop()

        forward_twists = get_twists(intersect_point, start, parent_f)
        backward_twists = get_twists(intersect_point, end, parent_b)

        return [*reversed(forward_twists), *inverse_twists(backward_twists)]


def get_twists(s, t, parent):
    twists = []
    while s != t:
        twists.append(parent[s][1])
        s = parent[s][0]
    return twists


def inverse_twists(twists):
    return [rubik.perm_inverse(twist) for twist in twists]
