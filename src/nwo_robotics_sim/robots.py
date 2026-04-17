from abc import ABC, abstractmethod
from typing import Dict, Any

class Robot(ABC):
    """Base robot class for simulation"""
    
    def __init__(self, name: str, robot_type: str):
        self.name = name
        self.robot_type = robot_type
        self.sensors: list = []
        self.actuators: list = []
        self.config: Dict[str, Any] = {}
    
    @abstractmethod
    def get_action_space(self):
        """Return available actions"""
        pass
    
    @abstractmethod
    def execute_action(self, action: str) -> bool:
        """Execute an action in simulation"""
        pass
    
    def add_sensor(self, sensor_type: str):
        """Add sensor to robot"""
        self.sensors.append(sensor_type)
    
    def add_actuator(self, actuator_type: str):
        """Add actuator to robot"""
        self.actuators.append(actuator_type)


class MobileManipulator(Robot):
    """Mobile manipulator robot (arm + base)"""
    
    def __init__(self):
        super().__init__("Mobile Manipulator", "mobile_manipulator")
        self.add_sensor("camera")
        self.add_sensor("lidar")
        self.add_actuator("base")
        self.add_actuator("arm")
        self.add_actuator("gripper")
    
    def get_action_space(self):
        return [
            "move_forward", "move_backward", "turn_left", "turn_right",
            "arm_up", "arm_down", "arm_extend", "arm_retract",
            "gripper_open", "gripper_close", "gripper_rotate"
        ]
    
    def execute_action(self, action: str) -> bool:
        if action in self.get_action_space():
            print(f"  [Robot] Executing: {action}")
            return True
        return False


class HumanoidRobot(Robot):
    """Humanoid robot"""
    
    def __init__(self):
        super().__init__("Humanoid", "humanoid")
        self.add_sensor("camera")
        self.add_sensor("imu")
        self.add_actuator("legs")
        self.add_actuator("arms")
    
    def get_action_space(self):
        return [
            "walk_forward", "walk_backward", "turn_left", "turn_right",
            "step_left", "step_right", "stand", "sit", "reach", "grasp"
        ]
    
    def execute_action(self, action: str) -> bool:
        if action in self.get_action_space():
            print(f"  [Robot] Executing: {action}")
            return True
        return False


class Drone(Robot):
    """Aerial drone robot"""
    
    def __init__(self):
        super().__init__("Drone", "drone")
        self.add_sensor("camera")
        self.add_sensor("gps")
        self.add_actuator("rotors")
    
    def get_action_space(self):
        return [
            "takeoff", "land", "hover",
            "move_up", "move_down", "move_forward", "move_backward",
            "rotate_cw", "rotate_ccw"
        ]
    
    def execute_action(self, action: str) -> bool:
        if action in self.get_action_space():
            print(f"  [Drone] Executing: {action}")
            return True
        return False