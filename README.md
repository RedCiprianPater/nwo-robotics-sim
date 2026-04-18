# NWO Robotics Simulation

[![PyPI](https://img.shields.io/pypi/v/nwo-robotics-sim.svg)](https://pypi.org/project/nwo-robotics-sim/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Local simulation bridge for NWO Robotics using LingBot-World world models.

## 🚀 Installation

```bash
pip install nwo-robotics-sim
```

## 📋 Requirements

- Python 3.10+
- CUDA-capable GPU (8GB+ VRAM recommended)
- PyTorch 2.4+

## 🎯 Quick Start

### Python API

```python
from nwo_robotics_sim import SimulationEnvironment
from nwo_robotics_sim.robots import MobileManipulator

# Create environment
env = SimulationEnvironment.create(
    name="warehouse",
    prompt="A warehouse with aisles and storage racks",
    size="480p"
)

# Load robot
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

### CLI Usage

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

## 🔗 Cloud Integration

This package works alongside the cloud API for remote simulation:

| Feature | Local (`nwo-sim`) | Cloud API |
|---------|------------------|-----------|
| **GPU Required** | Yes (your machine) | No (we provide) |
| **Cost** | Free | Pay-per-use |
| **Speed** | Depends on your GPU | High-performance |
| **Best For** | Development, testing | Production, scale |

**Cloud API:** https://nwo-simulation-api.onrender.com

## 🤖 Supported Robots

- **Mobile Manipulator** - Wheeled base with robotic arm
- **Humanoid** - Bipedal robot
- **Drone** - Aerial robot

## 🔧 Integration with NWO Robotics CLI

When both packages are installed, the `nwo` CLI automatically detects simulation capabilities:

```bash
# Via plugin (auto-detected)
nwo sim env create --name "test" --prompt "A test environment"
nwo sim run --env "test" --task "move forward"

# Or use local simulation flag
nwo robot "pick up box" --simulation

# Or use cloud API
nwo robot "pick up box" --remote
```

## 📦 Project Structure

```
nwo-robotics-sim/
├── src/nwo_robotics_sim/
│   ├── __init__.py          # Package entry point
│   ├── environment.py       # SimulationEnvironment class
│   ├── robots.py            # Robot definitions
│   ├── trainer.py           # RL training
│   ├── cli.py               # Command-line interface
│   └── plugin.py            # nwo-robotics plugin
├── setup.py                 # Package configuration
└── README.md                # This file
```

## 🌐 Links

- **PyPI:** https://pypi.org/project/nwo-robotics-sim/
- **GitHub:** https://github.com/RedCiprianPater/nwo-robotics-sim
- **Cloud API:** https://nwo-simulation-api.onrender.com
- **NWO Robotics:** https://github.com/nwocapital/nwo-robotics

## 📝 License

MIT License - See [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions welcome! Please open an issue or pull request on GitHub.

## ⚠️ Note

This is an alpha release. LingBot-World integration is scaffolded but requires manual setup of the world model weights for full functionality.