# Software roadmap

This working plan supports the [Lunar Hopper transition](https://uwjdr.atlassian.net/browse/JDR-51). See the [project overview](README.md) for the mission and demonstrator scope.

## 1. Carry forward the development foundation

The ROS 2 Jazzy workspace, ARM64 container build, and GitHub Actions checks provide the starting point. The existing tests check C++ and Python node startup and C++ to Python messaging. The [environment guide](environment/README.md) explains how to run them.

- Update the project documentation and the repository and test identifiers in [JDR-49](https://uwjdr.atlassian.net/browse/JDR-49) and [JDR-54](https://uwjdr.atlassian.net/browse/JDR-54).
- Extend the current C++ and Python CI checks in [JDR-53](https://uwjdr.atlassian.net/browse/JDR-53).
- Create the basic ROS 2 package in [JDR-55](https://uwjdr.atlassian.net/browse/JDR-55). The package milestone is a clean build and discovery by ROS 2.

## 2. Plan the standalone mapper and carrier

- Estimate the full payload's weight and power needs and document the mount and connections in [JDR-58](https://uwjdr.atlassian.net/browse/JDR-58).
- Use those estimates to compare the existing airframe with a prebuilt PX4-compatible option in [JDR-59](https://uwjdr.atlassian.net/browse/JDR-59).
- Retarget the ARM64 image and verify that it starts on the selected Jetson runtime in [JDR-52](https://uwjdr.atlassian.net/browse/JDR-52). Use the deployment script tracked in [JDR-47](https://uwjdr.atlassian.net/browse/JDR-47).

## 3. Define the demonstration

The proposed sequence is to verify standalone capture on the bench, then carry the module between scan sites with the drone and combine observations from overlapping viewpoints. The team still needs to agree on how scans are triggered, the map output, and what evidence will show the demo succeeded. Autonomous sequencing can follow the manually flown baseline.

The [previous SAR roadmap](https://github.com/RileyHop1/Lunar-Hopper/blob/665cfd7ad11caf90c4cba1583f458345bb0709cf/docs/software-roadmap.md) preserves the original development plan and diagram.
