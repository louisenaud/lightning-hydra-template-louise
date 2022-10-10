"""
File:        run.py
Created by:  louisenaud
On:          10/10/22
At:          2:22 PM
For project: lightning-hydra-template-louise
Description:
Usage:
"""
from pathlib import Path

import streamlit as st

import wandb
from src.models import TimmLitModule
from src.ui.core.serialization import load_model
from src.ui.core.utils import select_checkpoint


@st.cache(allow_output_mutation=True)
def get_model(checkpoint_path: Path):
    return load_model(module_class=TimmLitModule, checkpoint_path=checkpoint_path)


if wandb.api.api_key is None:
    st.error(
        "You are not logged in on `Weights and Biases`: https://docs.wandb.ai/ref/cli/wandb-login"
    )
    st.stop()

st.sidebar.subheader(f"Logged in W&B as: {wandb.api.viewer()['entity']}")

checkpoint_path = select_checkpoint()
model: TimmLitModule = get_model(checkpoint_path=checkpoint_path)
model
