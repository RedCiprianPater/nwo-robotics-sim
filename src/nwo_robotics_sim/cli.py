import click
from pathlib import Path
import json

from .environment import SimulationEnvironment
from .robots import MobileManipulator, HumanoidRobot, Drone

@click.group()
def main():
    """NWO Robotics Simulation CLI"""
    pass

@main.group()
def env():
    """Environment management"""
    pass

@env.command()
@click.option("--name", required=True, help="Environment name")
@click.option("--prompt", required=True, help="Environment description")
@click.option("--size", default="480p", help="Resolution (480p or 720p)")
@click.option("--type", "env_type", default="indoor", help="Environment type")
def create(name: str, prompt: str, size: str, env_type: str):
    """Create a new simulation environment"""
    click.echo(f"Creating environment: {name}")
    
    environment = SimulationEnvironment.create(
        name=name,
        prompt=prompt,
        size=size,
        env_type=env_type
    )
    
    # Save to local registry
    registry_path = Path("~/.nwo/registry/environments.json").expanduser()
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    
    registry = {}
    if registry_path.exists():
        with open(registry_path, "r") as f:
            registry = json.load(f)
    
    registry[environment.env_id] = {
        "name": name,
        "prompt": prompt,
        "size": size,
        "type": env_type,
        "status": environment.status
    }
    
    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2)
    
    click.echo(f"✓ Created: {environment.env_id}")

@env.command()
def list():
    """List all environments"""
    registry_path = Path("~/.nwo/registry/environments.json").expanduser()
    
    if not registry_path.exists():
        click.echo("No environments found")
        return
    
    with open(registry_path, "r") as f:
        registry = json.load(f)
    
    click.echo("\nEnvironments:")
    click.echo("-" * 60)
    for env_id, data in registry.items():
        click.echo(f"  {env_id}: {data['name']} ({data['size']}) - {data['status']}")

@main.command()
@click.option("--env", "env_id", required=True, help="Environment ID")
@click.option("--robot", default="mobile_manipulator", help="Robot type")
@click.option("--task", required=True, help="Task description")
@click.option("--duration", default=60, help="Simulation duration in seconds")
def run(env_id: str, robot: str, task: str, duration: int):
    """Run a simulation"""
    click.echo(f"Running simulation...")
    click.echo(f"  Environment: {env_id}")
    click.echo(f"  Robot: {robot}")
    click.echo(f"  Task: {task}")
    click.echo(f"  Duration: {duration}s")
    
    # Load environment
    registry_path = Path("~/.nwo/registry/environments.json").expanduser()
    with open(registry_path, "r") as f:
        registry = json.load(f)
    
    if env_id not in registry:
        click.echo(f"Error: Environment {env_id} not found")
        return
    
    # Create robot
    robot_map = {
        "mobile_manipulator": MobileManipulator,
        "humanoid": HumanoidRobot,
        "drone": Drone
    }
    
    robot_class = robot_map.get(robot, MobileManipulator)
    robot_instance = robot_class()
    
    # Load environment and run simulation
    env_data = registry[env_id]
    environment = SimulationEnvironment(
        env_id=env_id,
        name=env_data["name"],
        config=env_data
    )
    environment.status = env_data["status"]
    
    result = environment.simulate(robot_instance, task, duration)
    
    click.echo(f"\n✓ Simulation complete")
    click.echo(f"  Success: {result.success}")
    click.echo(f"  Metrics: {result.metrics}")

@main.command()
@click.option("--env", "env_ids", multiple=True, required=True, help="Environment ID(s)")
@click.option("--task", required=True, help="Training task")
@click.option("--robot", default="mobile_manipulator", help="Robot type")
@click.option("--episodes", default=1000, help="Number of training episodes")
@click.option("--algorithm", default="PPO", help="RL algorithm")
def train(env_ids: tuple, task: str, robot: str, episodes: int, algorithm: str):
    """Train a robot using reinforcement learning"""
    from .trainer import RobotTrainer
    
    click.echo(f"Starting training...")
    click.echo(f"  Environments: {', '.join(env_ids)}")
    click.echo(f"  Task: {task}")
    click.echo(f"  Episodes: {episodes}")
    click.echo(f"  Algorithm: {algorithm}")
    
    trainer = RobotTrainer(
        env_ids=list(env_ids),
        robot_type=robot,
        task=task,
        algorithm=algorithm
    )
    
    model_path = trainer.train(episodes=episodes)
    
    click.echo(f"\n✓ Training complete")
    click.echo(f"  Model saved: {model_path}")

if __name__ == "__main__":
    main()