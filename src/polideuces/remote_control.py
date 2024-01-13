import asyncio

import adapters.brain as abrain
import connectors.viam_robot as cviam
import connectors.xbox_gamepad as cxbox
import connectors.window_display as cwindow


SECRETS_FILE_NAME = "src/polideuces/secrets/credentials.json"
CONFIG_FILE_NAME = "src/polideuces/configs/polideuces-01.json"


async def init(secrets_file_name, config_file_name):
    robot = await cviam.ViamRobot().init(secrets_file_name, config_file_name)
    gamepad = cxbox.XBoxGamepad()
    window = cwindow.DisplayWindow(
        window_name="Polideuces-01", footers=["", "Press ESC to quit", "Pressione ESC para sair"]
    )

    return robot, gamepad, window


async def loop(robot, gamepad, window):
    # Step 1: Sense
    hor = gamepad.left_horizontal()
    acc = gamepad.right_trigger()
    rev = gamepad.left_trigger()
    lin_acc = await robot.accelerometer.get_linear_acceleration()
    frame = await robot.camera.get_image()

    # Step 2: Think
    x_acc, y_acc, z_acc = abrain.format_lin_acc(lin_acc)

    scale_factor = 2
    frame = abrain.format_frame(frame, scale_factor)

    max_speed = 1.0
    acceleration = abrain.get_acceleration(acc, rev)
    left_steer, right_steer = abrain.get_steer(hor)
    left_power, right_power = abrain.get_power(left_steer, right_steer, acceleration, max_speed)

    # Step 3: Act
    await robot.dc_motor_left.set_power(power=left_power)
    await robot.dc_motor_right.set_power(power=right_power)

    info = {
        "left steer": left_steer,
        "right steer": right_steer,
        "acceleration:": acceleration,
        "x acc": x_acc,
        "y acc": y_acc,
        "z acc": z_acc,
    }
    keep_loop = not window.update_frame(frame, info)

    return keep_loop


async def main():
    # Step1: Initiallize robot, gamepad and viewing window
    ctx = await init(SECRETS_FILE_NAME, CONFIG_FILE_NAME)

    # Step 2: Loop in sense-think-act framework
    keep_loop = True
    while keep_loop:
        keep_loop = await loop(*ctx)

    # Step 3: Close all elements
    for c in ctx:
        await c.close()


if __name__ == "__main__":
    asyncio.run(main())
