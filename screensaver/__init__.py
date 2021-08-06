import json
import os
import shlex
import itertools

import check50


@check50.check()
def valid():
    """project exists and is valid Scratch program"""

    # Make sure there is only one .sb2 file.
    filenames = [filename for filename in os.listdir() if filename.endswith(".sb3")]

    if len(filenames) > 1:
        raise check50.Failure("more than one .sb3 file found. Make sure there's only one!")
    elif not filenames:
        raise check50.Failure("no .sb3 file found")

    filename = filenames[0]

    # Ensure that unzipped .sb2 file contains .json file.
    if check50.run(f"unzip {shlex.quote(filename)}").exit():
        raise check50.Failure("invalid .sb3 file")
    check50.exists("project.json")

    with open("project.json") as f:
        project = json.load(f)

    return project["targets"]

