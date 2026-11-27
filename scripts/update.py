import argparse
import logging
import subprocess

logger = logging.getLogger(__name__)

image = "ghcr.io/rileyhop1/lunar-hopper-mission"
docker_name = "lunar-hopper"
docker_stable = "stable"


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "tag", nargs="?", help="This is the image that will be used"
    )

    parser.add_argument(
        "--local", help="Pull a specified local tag", action="store_true"
    )

    args = parser.parse_args()
    update(args.tag, args.local)


def deploy(tag):

    res = subprocess.run(
        ["docker", "ps", "-q", "-a", "--filter", f"name=^/{docker_name}$"],
        capture_output=True,
        text=True,
        check=True,
    )

    if res.stdout.strip():
        subprocess.run(["docker", "stop", f"{docker_name}"], check=True)
        subprocess.run(["docker", "rm", f"{docker_name}"], check=True)
    subprocess.run(
        [
            "docker",
            "run",
            "-d",
            "--pull=never",
            "--name",
            f"{docker_name}",
            f"{image}:{tag or 'latest'}",
        ],
        check=True,
    )


def update(tag="latest", local=False):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    logger.info("Running update")

    try:
        if not local:
            subprocess.run(
                ["docker", "pull", f"{image}:{tag or 'latest'}"], check=True
            )
        else:
            subprocess.run(
                ["docker", "image", "inspect", f"{image}:{tag or 'latest'}"],
                stdout=subprocess.DEVNULL,
                check=True,
            )

        deploy(tag)
        logger.info("Successful update")

    except subprocess.CalledProcessError as e:
        logger.error("Command failed: %s, exit code %s", e.cmd, e.returncode)
        res = subprocess.run(
            ["docker", "ps", "-q", "--filter", f"name=^/{docker_name}$"],
            capture_output=True,
            text=True,
            check=True,
        )

        if not res.stdout.strip():
            try:
                # Making the assumptions that the stable image exists, godly code
                deploy(docker_stable)

            except subprocess.CalledProcessError as e:
                logger.critical(
                    "Recovery failed: %s, exit code %s", e.cmd, e.returncode
                )
                raise


if __name__ == "__main__":
    main()
