# Lunar Hopper — A Terrain Mapping Demonstrator

Lunar Hopper is JDR's senior engineering project to demonstrate terrain mapping between sites. An Earth-based drone carries a detachable Jetson module with a camera and LiDAR. The drone's short flights stand in for lunar hops, and the module can collect data and build a terrain map on its own.

The project builds on the ROS 2 Jazzy development environment from the original search-and-rescue drone. See the [project overview](docs/README.md) for the new mission and prototype scope, and the [software roadmap](docs/software-roadmap.md) for open design decisions.

## Documentation

- [Documentation home](https://rileyhop1.github.io/SAR_DRONE/) for available published versions.
- [Development documentation](https://rileyhop1.github.io/SAR_DRONE/development/) for the project overview, software roadmap, and contributing guides.
- [Documentation source](docs/README.md) for the Markdown files in this repository.

## System overview

- **Carrier drone:** PX4 is the baseline for flight control. The team is comparing the existing airframe with a prebuilt PX4-compatible option.
- **Detachable mapper:** The Jetson module handles camera and LiDAR capture and terrain mapping. It can also operate on the bench.
- **Development:** ROS 2 Jazzy, Docker, and the existing CI checks support the transition.

## Repository structure

```text
.
├── packages/                     # ROS 2 Jazzy workspace
│   ├── sar_environment_test/      # Existing ROS 2 smoke tests
│   └── lunar_hopper_mapper/       # Planned basic package for the detachable mapper
├── docker/
│   └── mission.Dockerfile         # ARM64 image build used as the Jetson starting point
├── deployment/                   # Onboard deployment scripts and configuration
├── firmware/                     # Reserved for PX4 configuration and firmware work
├── scripts/
│   └── lint.py                    # Local and CI C++ checks
├── .github/
│   └── workflows/                 # ROS tests, documentation, and image publishing
├── docs/
│   ├── README.md                  # Lunar Hopper project overview
│   ├── environment/              # Development environment setup
│   └── software-roadmap.md        # Software milestones and dependencies
└── mkdocs.yml                    # Documentation site configuration
```

The basic mapper package setup is tracked in [JDR-55](https://uwjdr.atlassian.net/browse/JDR-55). The existing smoke-test package will get a Lunar Hopper name in [JDR-54](https://uwjdr.atlassian.net/browse/JDR-54).

## C++ checks

From the repository root in the Jazzy container, run `python3 scripts/lint.py packages` after building with compiler database generation enabled. See the [C++ linting guide](docs/cpp-linting.md) for tool installation, build commands, and formatting options.

## Build and deployment

Follow [the environment setup guide](docs/environment/README.md) to build the Jazzy workspace and run the existing tests. The current ARM64 build is the starting point for [Jetson deployment work](https://uwjdr.atlassian.net/browse/JDR-52).
