def find_treasure(pos, steps):
    (x, y) = pos
    if len(steps) == 0:
        return pos
    else:
        if steps[0] == 'up':
            steps.remove(steps[0])
            return find_treasure((x, y + 1), steps)
        elif steps[0] == 'down':
            steps.remove(steps[0])
            return find_treasure((x, y - 1), steps)
        elif steps[0] == 'right':
            steps.remove(steps[0])
            return find_treasure((x + 1, y), steps)
        elif steps[0] == 'left':
            steps.remove(steps[0])
            return find_treasure((x - 1, y), steps)
        
print(find_treasure((0, 0), ['up', 'up', 'left', 'right', 'up', 'up']))