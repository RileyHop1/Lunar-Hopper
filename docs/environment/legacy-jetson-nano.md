# Legacy Jetson Nano bring-up — Project Bullfrog Resurrection

On November 25, 2026, JDR brought an original Jetson Nano back into service as a temporary Lunar Hopper development platform while the Orin Nano hardware was unavailable. The goal is to develop ROS 2 packages and test Docker deployment, not to qualify this older board for flight or to assume equivalent performance.

## Hardware and approach

- Original Jetson Nano, believed to be the 4 GB A02 variant; exact revision still needs confirmation.
- 64 GB microSD card, macOS SD reader, monitor and keyboard.
- Community [Qengineering Jetson Nano Ubuntu 20.04 image](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image), using the older NVIDIA Tegra kernel and CUDA stack.

Docker provides a newer ROS 2 Jazzy userspace while sharing the legacy host kernel. This does not upgrade the kernel or NVIDIA drivers. The community image is not an official modern JetPack release; use only for isolated development, review its provenance and security limitations, and do not assume compatibility with modern GPU containers.

## Flash the microSD card from macOS

Download the appropriate image from the Qengineering project. The tested archive was `JetsonNanoUb20_3b.img.xz`. The following commands assume it is in Downloads.

```bash
# Install xz with Homebrew if it is missing.
brew install xz
xz -dk "$HOME/Downloads/JetsonNanoUb20_3b.img.xz"
ls -lh "$HOME/Downloads/JetsonNanoUb20_3b.img"
diskutil list
```

**Warning: dd destroys data on its destination.** Identify the removable SD card by size and device information, not by assuming the example disk number. Disconnect unrelated removable drives if possible. The identifier can change on reinsertion.

In our session the card was `/dev/disk5` (63.9 GB). Substitute your actual confirmed disk throughout.

```bash
diskutil info /dev/disk5
diskutil unmountDisk /dev/disk5
sudo dd if="$HOME/Downloads/JetsonNanoUb20_3b.img" of=/dev/rdisk5 bs=4m
sync
diskutil eject /dev/disk5
```

The SD reader initially reported `Media Read-Only: Yes`. Check the adapter's physical lock and try reinserting or changing the reader if needed; verify the correct device again. The exact cause of the lock was not established, but the subsequent write succeeded. Formatting or dd cannot override genuine hardware write protection.

Use Ctrl+T during dd on macOS to report progress. Wait for dd to finish before syncing and ejecting. The observed write was 31,281,119,232 bytes (7,458 records) in 731.75 seconds with no reported errors. No separate byte-for-byte readback was performed.

## Boot and verify the legacy CUDA environment

Insert the card into the Nano and power it using a suitable board power supply. Confirm the board reaches its desktop or shell.

```bash
cat /etc/os-release
uname -r
cat /etc/nv_tegra_release
/usr/local/cuda-10.2/bin/nvcc --version
cd /usr/local/cuda-10.2/samples/1_Utilities/deviceQuery
sudo make -j4
./deviceQuery
```

The board booted the community Ubuntu 20.04 image, reported Linux `4.9.253-tegra` and CUDA 10.2, and the operator reported `deviceQuery` passing. Exact L4T version and board revision were not recorded. deviceQuery verifies CUDA device enumeration; it is not a GPU computation benchmark.

## Run ROS 2 Jazzy in Docker

Docker was available on the booted image. Verify it first:

```bash
docker --version
sudo docker info
sudo docker run --rm hello-world
```

Then start the Jazzy container (no native Jazzy installation on the host is required):

```bash
sudo docker pull ros:jazzy-ros-base
sudo docker run --rm -it ros:jazzy-ros-base bash
```

Inside the container:

```bash
echo "$ROS_DISTRO"
ros2 topic list
exit
```

The operator reported successfully running ROS 2 Jazzy in the container. Exact image digest and command logs were not retained. For workspace bind mounts and ROS node tests, continue with [Start ROS 2 Jazzy](ros-jazzy.md) and [Verify Your Environment](verify.md). A successful ROS CLI invocation does not establish full DDS communications or camera access.

## Project deployment and remaining work

The same board subsequently pulled the Lunar Hopper mission image using a published commit tag, ran it to exit code 0, replaced the stopped container, deployed from the cache and recovered from a failed remote pull using a local stable image. See the [mission deployment guide](../deployment/mission-image.md) for commands, evidence limits and outstanding cases.

| Capability | Status |
| --- | --- |
| SD flash and host boot | Reported successful |
| CUDA device enumeration | Reported PASS |
| Docker and ROS 2 Jazzy container | Reported successful |
| Mission image deployment and basic recovery | Reported successful |
| Full ROS publisher/subscriber communication | Not verified in this bring-up |
| Actual GPU computation and GPU access inside Docker | Not verified |
| Camera capture and LiDAR integration | Not verified |
| Orin-equivalent performance or flight readiness | Not established |

The Nano can serve as a preliminary bench environment. Preserve a legacy-compatible hardware-access process if modern container GPU or camera integration proves incompatible, and validate any such interface before relying on it.

Tracking: [JDR-94](https://uwjdr.atlassian.net/browse/JDR-94), [JDR-93](https://uwjdr.atlassian.net/browse/JDR-93), [JDR-52](https://uwjdr.atlassian.net/browse/JDR-52), and [JDR-95](https://uwjdr.atlassian.net/browse/JDR-95).
