import math
import pygame
import logging


class XBoxGamepad:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        self.num_joysticks = pygame.joystick.get_count()

        if self.num_joysticks < 0:
            logging.info("No gamepad detected.")
            return

        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()
        logging.info(f"Gamepad connected: {self.gamepad.get_name()}")

        self.num_axes = self.gamepad.get_numaxes()
        self.num_buttons = self.gamepad.get_numbuttons()
        self.num_hats = self.gamepad.get_numhats()
        self.num_balls = self.gamepad.get_numballs()

        self.a_ind = 0
        self.b_ind = 1
        self.x_ind = 3
        self.y_ind = 4

        self.left_button_ind = 9
        self.right_button_ind = 10

        self.window_ind = 4
        self.xbox_ind = 5
        self.menu_ind = 6
        self.share_ind = 15

        self.left_horizontal_ind = 0
        self.left_vertical_ind = 1

        self.right_horizontal_ind = 2
        self.right_vertical_ind = 3

        self.left_trigger_ind = 4
        self.right_trigger_ind = 5

    async def close(self):
        pass

    def read_axis(self, axis_ind):
        pygame.event.pump()
        val = self.gamepad.get_axis(axis_ind)
        return round(val, 2)

    def read_analog(self, horizontal_ind, vertical_ind):
        horizontal = self.read_axis(horizontal_ind)
        vertical = self.read_axis(vertical_ind)

        mag = math.hypot(horizontal, vertical)
        mag = mag * (-1) ** (vertical > 0)  # Inverts on quadrant 3 and 4
        mag = round(mag, 2)
        if mag > 1.0:
            mag = 1.0

        angle = 0.0
        if vertical != 0:
            angle = -math.atan(horizontal / vertical)
            angle = angle * (-1) ** (vertical > 0)  # Inverts on quadrant 3 and 4
            angle = math.degrees(angle)
            angle = round(angle, 2)

        return mag, angle

    def read_button(self, button_ind):
        pygame.event.pump()
        return self.gamepad.get_button(button_ind)

    def read_all_axis(self):
        pygame.event.pump()
        axis = {i: int(100 * self.gamepad.get_axis(i)) for i in range(self.num_axes)}
        return axis

    def read_all_buttons(self):
        pygame.event.pump()
        buttons = {i: self.gamepad.get_button(i) for i in range(self.num_buttons)}
        return buttons

    def left_analog(self):
        return self.read_analog(self.left_horizontal_ind, self.left_vertical_ind)

    def right_analog(self):
        return self.read_analog(self.right_horizontal_ind, self.right_vertical_ind)

    def left_horizontal(self):
        return self.read_axis(self.left_horizontal_ind)

    def left_vertical(self):
        return self.read_axis(self.left_vertical_ind)

    def right_horizontal(self):
        return self.read_axis(self.right_horizontal_ind)

    def right_vertical(self):
        return self.read_axis(self.right_vertical_ind)

    def left_trigger(self):
        return self.read_axis(self.left_trigger_ind)

    def right_trigger(self):
        return self.read_axis(self.right_trigger_ind)
