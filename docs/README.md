# Lunar Hopper documentation

## Introduction

JDR is shifting its senior engineering project from a search-and-rescue drone to **Lunar Hopper — A Terrain Mapping Demonstrator**. The project uses an Earth-based drone to simulate movement between lunar scan sites.

The drone carries a detachable Jetson module with a camera and LiDAR. The module gathers observations from multiple viewpoints and combines them into a terrain map. It also operates independently on the bench.

[Firefly Aerospace’s Blue Ghost mission](https://www.nasa.gov/news-release/touchdown-carrying-nasa-science-fireflys-blue-ghost-lands-on-moon/) provides context for lunar surface science. [Intuitive Machines’ Grace hopper](https://www.nasa.gov/mission/polar-resources-ice-mining-experiment-1-prime-1/) is a reference for the planned use of hops to reach additional survey sites.

Read [Why we switched to Lunar Hopper](why-lunar-hopper.md) for the story behind the project.

## Project goals

- Demonstrate standalone camera and LiDAR operation on the Jetson module.
- Use short drone flights to move the module between overlapping viewpoints.
- Combine observations from multiple viewpoints into a terrain map and retain the underlying captures for review.

## Prototype scope

The team is planning an Earth-based demonstrator. Two short drone flights between three scan sites are a candidate demo sequence. Manual flight is the baseline. Autonomous hop sequencing is a stretch goal. The [hardware plan](https://uwjdr.atlassian.net/browse/JDR-58) and [carrier selection](https://uwjdr.atlassian.net/browse/JDR-59) track the open hardware decisions.

The ROS 2 Jazzy workspace, Docker setup, and existing tests carry forward. See the [software roadmap](software-roadmap.md) for the migration work and open decisions.

## Start here

New to the project? Follow [Setting Up Your Environment](environment/README.md) to prepare your development machine.

1. Read the introduction above and the [repository README](https://github.com/RileyHop1/SAR_DRONE) for the project and code layout.
2. Read the [software roadmap](software-roadmap.md) for goals, current work, and open decisions.
3. Follow the [Git conventions](git-conventions.md) for branches, commits, and pull requests.
4. Follow the [software development conventions](software-development-conventions.md) for interface documentation, tests, implementation, and review.
5. Follow the conventions for the language you are writing. [C++](cpp-conventions.md) · [Python](python-conventions.md)

## Proposed website sections

This is a provisional navigation structure for team review. Entries marked planned describe pages to develop.

| Section | What readers should find | Current material |
| --- | --- | --- |
| Project overview | Purpose, goals, scope, and mission workflow | This home page |
| Getting started | Required tools, local setup, container builds, first ROS run, and troubleshooting | [Environment setup](environment/README.md) |
| Architecture and interfaces | System diagram, package structure, message definitions, and design decisions | New architecture to be scoped |
| Development guide | Git workflow, documentation-first development, testing workflow, naming, and formatting | [Git](git-conventions.md), [development](software-development-conventions.md), [C++](cpp-conventions.md), and [Python](python-conventions.md) conventions |
| Simulation and testing | Simulation setup, test commands, scenarios, and results | Practical guides planned |
| Deployment and operation | Prototype setup and operation, health checks, and map and data retrieval | Planned |
| Roadmap and project status | Major goals, dependencies, open decisions, and verified progress | [Software roadmap](software-roadmap.md) |

## Previous project documentation

The following working documents describe the original search-and-rescue mission and preserve the context for earlier design and test decisions. The Lunar Hopper transition is tracked in [JDR-51](https://uwjdr.atlassian.net/browse/JDR-51).

- **PRD_SAR_DRONE.docx** describes user needs, product goals, scope, constraints, and proposed release criteria.
- **DESIGN_SPEC_SAR_DRONE.docx** describes system responsibilities, architecture, interfaces, and implementation details to develop.
- **TEST_PLAN_SAR_DRONE.docx** describes test configurations, scenarios, evidence, and staged validation.

## Adding and maintaining documentation

- Put project documentation in this folder using descriptive lowercase filenames with hyphens.
- Begin each document with its purpose and enough context for a new teammate.
- Link new documents from this README with a short description.
- Use relative Markdown links between repository files so they work across branches and checkouts.
- Keep each convention in its dedicated document and link to it from related guides.
- Distinguish agreed decisions, proposals, and open questions.
- Update documentation with the behavior or interface change it describes.
- Include prerequisites, commands, and expected results in setup or verification instructions.
- Cite external references and record relevant decisions so teammates can trace their context.
- Review documentation through the branch and PR process described in the Git conventions.

These Markdown files supply the GitHub Pages documentation website.
