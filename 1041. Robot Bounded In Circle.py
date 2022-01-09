def move(position, direction):
    if direction == 'N':
        position[1] += 1
    elif direction == 'S':
        position[1] -= 1
    elif direction == 'E':
        position[0] += 1
    elif direction == 'W':
        position[0] -= 1
    return position

def change_direction(current, turn):
    if current == 'N':
        if turn == 'L':
            return 'W'
        if turn == 'R':
            return 'E'
    if current == 'W':
        if turn == 'L':
            return 'S'
        if turn == 'R':
            return 'N'
    if current == 'S':
        if turn == 'L':
            return 'E'
        if turn == 'R':
            return 'W'
    if current == 'E':
        if turn == 'L':
            return 'N'
        if turn == 'R':
            return 'S'
    

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        direction = 'N'
        position = [0,0]
        for i in range(4):
            for ins in instructions:
                if ins == 'G':
                    position = move(position, direction)
                else:
                    direction = change_direction(direction, ins)
            if position == [0,0]:
                return True

        return False