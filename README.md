# NWO Robotics Simulation

Local simulation bridge for NWO Robotics using LingBot-World.

## Installation

```bash
pip install nwo-robotics-sim
```

## Requirements

- Python 3.10+
- CUDA-capable GPU (8GB+ VRAM)
- PyTorch 2.4+

## Quick Start

```python
from nwo_robotics_sim import SimulationEnvironment

# Create environment
env = SimulationEnvironment.create(
    name="warehouse",
    prompt="A warehouse with aisles and storage racks",
    size="480p"
)

# Load robot
from nwo_robotics_sim.robots import MobileManipulator
robot = MobileManipulator()

# Run simulation
result = env.simulate(
    robot=robot,
    task="navigate to shelf A3 and pick up box",
    duration=60
)

# View results
result.show_video()
print(result.metrics)
```

## CLI Usage

```bash
# Create environment
nwo-sim env create --name "warehouse" --prompt "A warehouse"

# List environments
nwo-sim env list

# Run simulation
nwo-sim run --env "warehouse" --robot "mobile_manipulator" --task "pick up box"

# Train robot
nwo-sim train --env "warehouse" --task "navigation" --episodes 1000
```

## Integration with NWO Robotics CLI

When both packages are installed:

```bash
nwo robot "pick up box" --simulation  # Uses local simulation
nwo robot "pick up box" --remote      # Uses cloud API
```

## License

MIT