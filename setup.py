from setuptools import setup, find_packages

setup(
    name="nwo-robotics-sim",
    version="0.1.0",
    description="Local simulation bridge for NWO Robotics using LingBot-World",
    author="NWO Robotics",
    author_email="ciprian.pater@publicae.org",
    packages=find_packages(),
    install_requires=[
        "torch>=2.4.0",
        "numpy>=1.26.0",
        "pillow>=10.0.0",
        "click>=8.1.0",
        "nwo-robotics>=2.0.0",
    ],
    extras_require={
        "lingbot": [
            "flash-attn",
            "transformers>=4.35.0",
        ],
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nwo-sim=nwo_robotics_sim.cli:main",
        ],
        "nwo_robotics.plugins": [
            "simulation=nwo_robotics_sim.plugin:SimulationPlugin",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)