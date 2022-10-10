"""
File:        __init__.py
Created by:  louisenaud
On:          10/10/22
At:          2:17 PM
For project: lightning-hydra-template-louise
Description:
Usage:
From: https://github.com/grok-ai/nn-template-core
"""
import logging
import os
from pathlib import Path

import git

from .common import load_envs

logger = logging.getLogger(__name__)


# Load environment variables
load_envs()

try:
    PROJECT_ROOT = Path(git.Repo(Path.cwd(), search_parent_directories=True).working_dir)
except git.exc.InvalidGitRepositoryError:
    PROJECT_ROOT = Path.cwd()

logger.debug(f"Inferred project root: {PROJECT_ROOT}")
os.environ["PROJECT_ROOT"] = str(PROJECT_ROOT)
