# Snake Game using dudraw and a DoublyLinkedList
# Controls: W = up, A = left, S = down, D = right
#Reed Braunfeld 4/14/2026 Comp 1353



import dudraw
import random


# -- Doubly Linked List --

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        values = []
        current = self._head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values)

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def add_first(self, v):
        new_node = Node(v)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def add_last(self, v):
        new_node = Node(v)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Can't remove from an empty list")
        value = self._head.value
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Can't remove from an empty list")
        value = self._tail.value
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._head.value

    def last(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._tail.value

    def search(self, v):
        current = self._head
        index = 0
        while current:
            if current.value == v:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        current = self._head
        for _ in range(i):
            current = current.next
        return current.value


# -- DLL test 

def dll_tester():
    test_list = DoublyLinkedList()

    assert test_list.get_size() == 0, 'list should be empty to start!'

    test_list.add_first(1)
    assert test_list.first() == 1,     'add_first needs adjustment!'
    assert test_list.last() == 1,      'add_first needs adjustment!'
    assert test_list.get_size() == 1,  'add_first needs adjustment!'
    test_list.add_first(2)
    assert test_list.first() == 2,     'add_first needs adjustment!'
    assert test_list.last() == 1,      'add_first needs adjustment!'
    assert test_list.get_size() == 2,  'add_first needs adjustment!'

    test_list.add_last(3)
    assert test_list.first() == 2,     'add_last needs adjustment!'
    assert test_list.last() == 3,      'add_last needs adjustment!'
    assert test_list.get_size() == 3,  'add_last needs adjustment!'

    assert test_list.remove_first() == 2, 'remove_first needs adjustment!'
    assert test_list.first() == 1,        'remove_first needs adjustment!'
    assert test_list.last() == 3,         'remove_first needs adjustment!'
    assert test_list.get_size() == 2,     'remove_first needs adjustment!'

    assert test_list.remove_last() == 3,  'remove_last needs adjustment!'
    assert test_list.first() == 1,        'remove_last needs adjustment!'
    assert test_list.last() == 1,         'remove_last needs adjustment!'
    assert test_list.get_size() == 1,     'remove_last needs adjustment!'

    while not test_list.is_empty():
        test_list.remove_first()

    assert test_list.get_size() == 0, 'list should be empty after removing all values'

    for i in range(10):
        test_list.add_last(i + 1)

    assert test_list.get(0) == 1,  'get(0) should return the element at first index'
    assert test_list.get(5) == 6,  'get(5) should return the element at index 5'
    assert test_list.get(9) == 10, 'get(9) should return the element at last index'

    print('All tests passed!')


#################

GRID_SIZE = 20   # how many cells across and tall the board is
HALF      = 0.5  # used to center things inside a cell

# colors constants
COLOR_BG         = (15,  15,  30)
COLOR_GRID       = (30,  30,  50)
COLOR_SNAKE_HEAD = (80,  220, 100)
COLOR_SNAKE_BODY = (50,  160, 70)
COLOR_FOOD       = (230, 60,  60)
COLOR_TEXT       = (220, 220, 220)


# The Food (apple!) 

class Food:
    def __init__(self, snake_segments):
        self.x = 0
        self.y = 0
        self.respawn(snake_segments)

    def respawn(self, snake_segments):
        # build a set of cells the snake is already on, then pick somewhere else
        occupied = set()
        for i in range(snake_segments.get_size()):
            occupied.add(snake_segments.get(i))

        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if (x, y) not in occupied:
                self.x = x
                self.y = y
                break

    def draw(self):
        cx = self.x + HALF
        cy = self.y + HALF
        dudraw.set_pen_color_rgb(180, 40, 40)       # dark outer ring
        dudraw.filled_circle(cx, cy, HALF * 0.75)
        dudraw.set_pen_color_rgb(*COLOR_FOOD)        # bright red center
        dudraw.filled_circle(cx, cy, HALF * 0.55)
        dudraw.set_pen_color_rgb(255, 180, 180)      # little shine dot
        dudraw.filled_circle(cx + 0.12, cy + 0.12, HALF * 0.15)


# The Snake

class Snake:
    def __init__(self):
        # body is stored head-first as (x, y) tuples in a doubly linked list
        self.segments = DoublyLinkedList()
        cx = GRID_SIZE // 2
        cy = GRID_SIZE // 2
        self.segments.add_last((cx,     cy))
        self.segments.add_last((cx - 1, cy))
        self.segments.add_last((cx - 2, cy))

        self.dx = 1    # start moving right
        self.dy = 0
        self.grow = False  # set to True when food is eaten

    def set_direction(self, dx, dy):
        # ignore the input if it would reverse us straight into our own neck
        if dx == -self.dx and dy == -self.dy:
            return
        self.dx = dx
        self.dy = dy

    def move(self):
        hx, hy = self.segments.first()
        self.segments.add_first((hx + self.dx, hy + self.dy))

        if self.grow:
            self.grow = False  # keep the tail this turn so we get one longer
        else:
            self.segments.remove_last()

    def eat(self):
        self.grow = True

    def head(self):
        return self.segments.first()

    def hits_wall(self):
        hx, hy = self.head()
        return hx < 0 or hx >= GRID_SIZE or hy < 0 or hy >= GRID_SIZE

    def hits_self(self):
        hx, hy = self.head()
        for i in range(1, self.segments.get_size()):
            if self.segments.get(i) == (hx, hy):
                return True
        return False

    def draw(self):
        size = self.segments.get_size()
        for i in range(size):
            x, y = self.segments.get(i)
            cx = x + HALF
            cy = y + HALF

            if i == 0:
                dudraw.set_pen_color_rgb(*COLOR_SNAKE_HEAD)
                dudraw.filled_square(cx, cy, HALF * 0.92)

                # draw eyes facing whichever way we're moving
                dudraw.set_pen_color_rgb(0, 0, 0)
                off = 0.22
                if self.dx == 1:
                    dudraw.filled_circle(cx + 0.25, cy + off, 0.08)
                    dudraw.filled_circle(cx + 0.25, cy - off, 0.08)
                elif self.dx == -1:
                    dudraw.filled_circle(cx - 0.25, cy + off, 0.08)
                    dudraw.filled_circle(cx - 0.25, cy - off, 0.08)
                elif self.dy == 1:
                    dudraw.filled_circle(cx + off, cy + 0.25, 0.08)
                    dudraw.filled_circle(cx - off, cy + 0.25, 0.08)
                else:
                    dudraw.filled_circle(cx + off, cy - 0.25, 0.08)
                    dudraw.filled_circle(cx - off, cy - 0.25, 0.08)
            else:
                # fade the body color toward the tail so it looks a bit nicer
                ratio = 1.0 - (i / size) * 0.5
                r = int(COLOR_SNAKE_BODY[0] * ratio)
                g = int(COLOR_SNAKE_BODY[1] * ratio)
                b = int(COLOR_SNAKE_BODY[2] * ratio)
                dudraw.set_pen_color_rgb(r, g, b)
                dudraw.filled_square(cx, cy, HALF * 0.85)


#Helper (Drawing)

def draw_background():
    dudraw.set_pen_color_rgb(*COLOR_BG)
    dudraw.filled_rectangle(GRID_SIZE / 2, GRID_SIZE / 2, GRID_SIZE / 2, GRID_SIZE / 2)
    dudraw.set_pen_color_rgb(*COLOR_GRID)
    dudraw.set_pen_width(0.5)
    for i in range(GRID_SIZE + 1):
        dudraw.line(i, 0, i, GRID_SIZE)
        dudraw.line(0, i, GRID_SIZE, i)
    dudraw.set_pen_width(1)


def draw_border():
    dudraw.set_pen_color_rgb(80, 200, 120)
    dudraw.set_pen_width(3)
    dudraw.rectangle(GRID_SIZE / 2, GRID_SIZE / 2, GRID_SIZE / 2, GRID_SIZE / 2)
    dudraw.set_pen_width(1)


def draw_score(score):
    dudraw.set_pen_color_rgb(*COLOR_TEXT)
    dudraw.set_font_size(18)
    dudraw.text(GRID_SIZE / 2, GRID_SIZE - 0.6, f"Score: {score}")


def draw_game_over(score):
    dudraw.set_pen_color_rgb(10, 10, 20)
    dudraw.filled_rectangle(GRID_SIZE / 2, GRID_SIZE / 2, GRID_SIZE / 2 - 1, 3)
    dudraw.set_pen_color_rgb(230, 60, 60)
    dudraw.set_font_size(28)
    dudraw.text(GRID_SIZE / 2, GRID_SIZE / 2 + 1.2, "GAME OVER")
    dudraw.set_pen_color_rgb(*COLOR_TEXT)
    dudraw.set_font_size(18)
    dudraw.text(GRID_SIZE / 2, GRID_SIZE / 2 - 0.2, f"Final Score: {score}")
    dudraw.set_font_size(14)
    dudraw.text(GRID_SIZE / 2, GRID_SIZE / 2 - 1.4, "Close the window to exit")


#MAIN! 

def main():
    dll_tester()

    dudraw.set_canvas_size(600, 600)
    dudraw.set_x_scale(0, GRID_SIZE)
    dudraw.set_y_scale(0, GRID_SIZE)

    snake = Snake()
    food  = Food(snake.segments)
    score = 0
    game_over = False

    # buffer the next direction so fast inputs aren't dropped between frames
    next_dx = snake.dx
    next_dy = snake.dy

    limit = 12  # lower this to make the snake move faster
    timer = 0

    while True:
        timer += 1

        if not game_over:
            if dudraw.has_next_key_typed():
                key = dudraw.next_key_typed()
                if key == 'w' and snake.dy != -1:
                    next_dx, next_dy = 0,  1
                elif key == 's' and snake.dy != 1:
                    next_dx, next_dy = 0, -1
                elif key == 'a' and snake.dx != 1:
                    next_dx, next_dy = -1, 0
                elif key == 'd' and snake.dx != -1:
                    next_dx, next_dy = 1,  0

        if timer == limit:
            timer = 0

            if not game_over:
                snake.set_direction(next_dx, next_dy)
                snake.move()

                if snake.hits_wall() or snake.hits_self():
                    game_over = True

                if not game_over:
                    hx, hy = snake.head()
                    if hx == food.x and hy == food.y:
                        snake.eat()
                        score += 1
                        food.respawn(snake.segments)

            draw_background()
            draw_border()
            food.draw()
            snake.draw()
            draw_score(score)

            if game_over:
                draw_game_over(score)

            dudraw.show(40)

        else:
            dudraw.show(5)


if __name__ == "__main__":
    main()