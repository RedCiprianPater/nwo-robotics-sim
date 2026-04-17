"""
Plugin for nwo-robotics CLI
"""

import click
from typing import Optional

class SimulationPlugin:
    """Plugin to add simulation commands to nwo-robotics CLI"""
    
    name = "simulation"
    version = "0.1.0"
    
    @staticmethod
    def register(cli_group):
        """Register simulation commands with the main CLI"""
        
        @cli_group.group()
        def sim():
            """Simulation mode (requires nwo-robotics-sim)"""
            pass
        
        @sim.group()
        def env():
            """Environment management"""
            pass
        
        @env.command()
        @click.option("--name", required=True)
        @click.option("--prompt", required=True)
        @click.option("--size", default="480p")
        def create(name, prompt, size):
            """Create environment"""
            from ..cli import env as env_cmd
            ctx = click.Context(env_cmd)
            ctx.invoke(env_cmd.commands["create"], name=name, prompt=prompt, size=size, type="indoor")
        
        @env.command()
        def list():
            """List environments"""
            from ..cli import env as env_cmd
            ctx = click.Context(env_cmd)
            ctx.invoke(env_cmd.commands["list"])
        
        @sim.command()
        @click.option("--env", "env_id", required=True)
        @click.option("--robot", default="mobile_manipulator")
        @click.option("--task", required=True)
        @click.option("--duration", default=60)
        def run(env_id, robot, task, duration):
            """Run simulation"""
            from ..cli import main
            ctx = click.Context(main)
            ctx.invoke(main.commands["run"], env_id=env_id, robot=robot, task=task, duration=duration)
        
        @sim.command()
        @click.option("--env", "env_ids", multiple=True, required=True)
        @click.option("--task", required=True)
        @click.option("--robot", default="mobile_manipulator")
        @click.option("--episodes", default=1000)
        def train(env_ids, task, robot, episodes):
            """Train robot"""
            from ..cli import main
            ctx = click.Context(main)
            ctx.invoke(main.commands["train"], env_ids=env_ids, task=task, robot=robot, episodes=episodes, algorithm="PPO")

# Entry point for plugin discovery
def get_plugin():
    return SimulationPlugin()