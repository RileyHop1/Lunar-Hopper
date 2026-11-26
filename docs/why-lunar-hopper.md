# Why we switched to Lunar Hopper

We started with a search-and-rescue drone. We thought it would be a genuinely cool capstone. We could build a drone that would cover a search area and use onboard sensors to help spot someone who needed help. It gave us a reason to learn flight control, robotics software, and sensing as parts of one system.

Then one of our project mentors showed us what NASA and its industry partners were working on for the Moon. The idea that got us talking was [Grace, Intuitive Machines’ Micro Nova Hopper](https://www.nasa.gov/mission/polar-resources-ice-mining-experiment-1-prime-1/). Grace was designed to hop into a permanently shadowed crater and take measurements there. A single move could put the instruments somewhere with an entirely different view.

That sent our capstone planning in a new direction. *What could we learn about a patch of terrain if we could pick up our sensors and hop to a better spot?* We’re all space enthusiasts, so that question stuck. It also gave us a more original problem to work on and a result other teams could build on. A detachable mapping module could be picked up, moved, and used on its own.

## What we’re building

**Lunar Hopper** is an Earth-based terrain mapping demonstrator. A drone carries a detachable module with a camera, LiDAR, and a Jetson computer. Short flights stand in for lunar hops. Each stop gives the module a new view, and the goal is to combine those views into one terrain map. The same module can collect data and map on the bench, independently of the drone.

The search-and-rescue plan gave us a head start on flight control and the ROS 2 development setup. Now we get to use that work to find out how much a new viewpoint can add to the map.

See the [project overview](README.md) for the demonstrator’s scope and the [software roadmap](software-roadmap.md) for what we’re planning next.
