# Mission image deployment and startup

This guide describes the Python deployment scripts from [JDR-47](https://uwjdr.atlassian.net/browse/JDR-47) and [PR #25](https://github.com/RileyHop1/Lunar-Hopper/pull/25). At the time of the November 25 bench test, the scripts were on the feature branch and not yet merged into Development.

## Prerequisites

- Linux ARM64 test machine with Docker Engine running and Python 3.7 or newer.
- Access to the GitHub Container Registry (GHCR) and a published ARM64 mission image tag.
- A checkout containing `scripts/update.py` and `scripts/startup.py`.
- Permission to use Docker. The examples use `sudo` when needed.
- An isolated bench machine: the script stops and removes the existing container named `lunar-hopper`. Data in that container's writable layer is lost.

The mission image is `ghcr.io/rileyhop1/lunar-hopper-mission`. Find available tags on the [package page](https://github.com/users/RileyHop1/packages/container/package/lunar-hopper-mission) or in the successful publishing workflow logs. Do not assume that a Git commit automatically has a corresponding published image.

To test the unmerged implementation:

```bash
git clone -b JDR-47-python-docker-script https://github.com/RileyHop1/Lunar-Hopper.git
cd Lunar-Hopper
```

Once the scripts have merged, use the appropriate current checkout instead.

## Command-line usage

Run from the repository root. Replace `YOUR_PUBLISHED_TAG` with an actual published tag; the variable is not a literal image tag.

```bash
TAG=YOUR_PUBLISHED_TAG
sudo python3 scripts/update.py "$TAG"
sudo docker ps -a --filter name=lunar-hopper
sudo docker logs lunar-hopper
```

| Command | Behavior |
| --- | --- |
| `python3 scripts/update.py` | Pull and deploy `latest`. |
| `python3 scripts/update.py TAG` | Pull and deploy the specified remote tag. |
| `python3 scripts/update.py --local TAG` | Inspect and deploy an already cached tag without pulling. |
| `python3 scripts/update.py --local` | Inspect and deploy cached `latest`. |
| `python3 scripts/startup.py` | Call `update()` with its defaults (remote `latest`). |

Use the same privilege context for Docker and Python. The startup wrapper is an entry point, not a configured boot service; automatic launch at host boot would require additional service configuration and testing.

## How the update works

1. Resolve an omitted or empty tag to `latest`.
2. Pull the requested remote image, or inspect it locally when `--local` is specified.
3. Find an existing container named exactly `lunar-hopper` (including stopped containers). Stop and remove it if found.
4. Launch the selected image in detached mode using `docker run -d --pull=never --name lunar-hopper IMAGE:TAG`.
5. Log successful completion of the Docker launch command.

The script catches Docker subprocess failures. It checks whether the named container is currently running. If it is running, the script leaves it alone rather than attempting fallback. Otherwise, it attempts to deploy the local `stable` tag. If that deployment raises a Docker subprocess error, the script logs a critical failure and re-raises it.

The script does not guarantee rollback after a replacement has stopped the previous container. It also does not check whether the new process remains running or whether ROS is healthy. A failed update can return normally if an existing container remains running or fallback succeeds.

## Test local recovery

After checking the selected image, designate it as stable manually. Do this only on a bench system.

```bash
IMAGE=ghcr.io/rileyhop1/lunar-hopper-mission
TAG=YOUR_PUBLISHED_TAG
sudo docker tag "$IMAGE:$TAG" "$IMAGE:stable"
sudo python3 scripts/update.py --local "$TAG"
sudo python3 scripts/update.py bullfrog-nonexistent-test-tag
sudo docker ps -a --filter name=lunar-hopper
sudo docker inspect --format '{{.Config.Image}} {{.State.Status}} {{.State.ExitCode}}' lunar-hopper
```

The deliberately nonexistent tag should fail to pull. If no mission container is running, recovery should launch the cached `stable` image. If a mission container is running, the script should preserve it instead. Confirm the actual image and state, not just the script's exit status. Stable promotion is manual; a cached image is not automatically known-good.

## November 25 bench results

The following observations were reported by the operator on the [legacy Jetson Nano](../environment/legacy-jetson-nano.md) during [JDR-93](https://uwjdr.atlassian.net/browse/JDR-93). Raw test logs were not collected for this guide.

| Scenario | Result |
| --- | --- |
| Remote deployment with an explicit published tag | Pass; container executed and exited with code 0. |
| Repeat deployment over a stopped container | Pass. |
| Local cached image deployment | Pass. |
| Missing remote tag with no running container and cached stable | Pass; stable recovery reported successful. |
| Default remote latest | Blocked; registry returned `manifest unknown`. |
| Running-container replacement and preservation on failed pull/local lookup | Not yet verified. |
| Recovery without a stable image; startup wrapper; comprehensive logging checks | Not yet verified. |

The current Dockerfile uses `CMD ["bash"]`; a detached noninteractive shell can exit normally. Exit 0 does not demonstrate a long-running mission service. [JDR-95](https://uwjdr.atlassian.net/browse/JDR-95) tracks the persistent ROS 2 mission node and outstanding regression tests. The publishing change in PR #25 adds a `latest` tag alongside the commit SHA; it was not available during this bench test.

## Troubleshooting

- `manifest unknown`: check the exact image name and published tag.
- `no matching manifest` or architecture mismatch: verify the registry has a compatible Linux ARM64 image.
- Registry permission errors: check package visibility and authentication; do not publish credentials.
- Docker launch exits immediately: inspect `docker ps -a`, the exit code and logs. A successful Docker run is not a health check.

No flight-readiness claim is made by these bench tests.
