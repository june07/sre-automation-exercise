"""Module to calculate debian package statistics."""
import os
import gzip
import hashlib
import argparse
import requests

def download(args):
    """Function to download debian package and return md5 hash of the downloaded file."""
    # Construct the URL for the Contents file
    url = f"http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{args['arch']}.gz"

    # Download the file
    request = requests.get(url)
    request.raise_for_status()

    # Write the contents to a file
    with open(f"Contents-{args['arch']}.gz", "wb") as file:
        file.write(request.content)

    # Decompress the file
    with gzip.open(f"Contents-{args['arch']}.gz", "rb") as f_in, open(
        f"Contents-{args['arch']}", "wb"
    ) as f_out:
        f_out.write(f_in.read())

    os.remove(f"Contents-{args['arch']}.gz")

    return hashlib.md5(request.content).hexdigest()

def main(args):
    """Main function to calculate debian package stats."""
    # do not download while testing as the files are copied from tests
    if __name__ == "__main__":
        download(args)
    else:
        print(f"Skipping download in test environment.")

    # Parse the file and get the statistics
    stats = {}
    with open(f"Contents-{args['arch']}") as file:
        for line in file:
            packages = line.split()[1].split(",")
            for package in packages:
                if package in stats:
                    stats[package] += 1
                else:
                    stats[package] = 1

    output = ""
    # Sort the statistics and output the top 10 packages
    sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        package, count = sorted_stats[i]
        print(f"{i+1}. {package}: {count}")
        output += f"{i+1}. {package}: {count}\n"

    # Clean up
    os.remove(f"Contents-{args['arch']}")
    return output


if __name__ == "__main__":
    # Parse the command line arguments
    PARSER = argparse.ArgumentParser(
        description="Download and parse the compressed Contents file for a specific architecture"
    )
    PARSER.add_argument(
        "arch", type=str, help="The architecture (amd64, arm64, mips, etc.)"
    )
    ARGS = PARSER.parse_args()
    main(vars(ARGS))
