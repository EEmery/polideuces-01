import json

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.board import Board
from viam.components.servo import Servo
from viam.components.motor import Motor
from viam.components.movement_sensor import MovementSensor
from viam.components.camera import Camera


class ViamRobot:
    def __init__(self):
        self.robot = None

    async def init(self, secrets_file_name, config_file_name):
        address, credential = self._get_creds(secrets_file_name)
        self.robot = await self._connect(address, credential)
        self._init_components(self.robot, config_file_name)

        return self

    async def close(self):
        await self.robot.close()

    def _get_creds(self, secrets_file_name):
        with open(secrets_file_name, "r") as f:
            secret = json.load(f)

        return secret["address"], secret["credential"]

    async def _connect(self, address, credential):
        creds = Credentials(type="robot-location-secret", payload=credential)
        opts = RobotClient.Options(refresh_interval=0, dial_options=DialOptions(credentials=creds))
        return await RobotClient.at_address(address, opts)

    def _init_components(self, robot, config_file_name):
        with open(config_file_name, "r") as f:
            config_data = json.load(f)
            components_data = config_data.get("components")

            for component_data in components_data:
                cname = self._to_snake_case(component_data["name"])
                ctype = component_data["type"]

                component = self._handle(ctype)(robot, component_data)

                setattr(self, cname, component)

    def _to_snake_case(self, s):
        return s.lower().replace("-", "_")

    def _handle(self, ctype):
        handlers = {
            "motor": self._handle_motor,
            "servo": self._handle_servo,
            "camera": self._handle_camera,
            "movement_sensor": self._handle_movement_sensor,
        }

        try:
            return handlers[ctype]
        except KeyError:
            return self._handle_unimplemented

    def _handle_unimplemented(self, _, __):
        return None

    def _handle_board(self, robot, component_data):
        cname = component_data["name"]
        return Board.from_robot(robot, cname)

    def _handle_motor(self, robot, component_data):
        cname = component_data["name"]
        return Motor.from_robot(robot, cname)

    def _handle_servo(self, robot, component_data):
        cname = component_data["name"]
        return Servo.from_robot(robot, cname)

    def _handle_camera(self, robot, component_data):
        cname = component_data["name"]
        return Camera.from_robot(robot, cname)

    def _handle_movement_sensor(self, robot, component_data):
        cname = component_data["name"]
        return MovementSensor.from_robot(robot, cname)
