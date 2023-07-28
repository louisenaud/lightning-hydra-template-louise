<div align="center">

# Pytorch Lightning / Hydra / Timm Template

[![python](https://img.shields.io/badge/-Python_3.7_%7C_3.8_%7C_3.9_%7C_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pytorch](https://img.shields.io/badge/PyTorch_1.8+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![lightning](https://img.shields.io/badge/-Lightning_1.6+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Config-Hydra_1.2-89b8cd)](https://hydra.cc/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![pre-commit](https://img.shields.io/badge/Pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![tests](https://github.com/louisenaud/lightning-hydra-template-louise/actions/workflows/test.yml/badge.svg)](https://github.com/louisenaud/lightning-hydra-template-louise/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/louisenaud/lightning-hydra-template-louise/branch/main/graph/badge.svg)](https://codecov.io/gh/louisenaud/lightning-hydra-template-louise)
[![code-quality](https://github.com/louisenaud/lightning-hydra-template-louise/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/louisenaud/lightning-hydra-template-louise#license)
[![contributors](https://img.shields.io/github/contributors/louisenaud/lightning-hydra-template-louise.svg)](https://github.com/louisenaud/lightning-hydra-template-louise/graphs/contributors)
<a href="https://github.com/louisenaud/lightning-hydra-template-louise"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>

<div align="center">

</div>

## Description

Pytorch lightning + Hydra + Timm models template.

## Main Technologies

[PyTorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning) - a lightweight PyTorch wrapper for
high-performance AI research. Think of it as a framework for organizing your PyTorch code.

[Hydra](https://github.com/facebookresearch/hydra) - a framework for elegantly configuring complex applications. The key
feature is the ability to dynamically create a hierarchical configuration by composition and override it through config
files and the command line.

<br>

## Main Ideas Of This Template

- **Predefined Structure**: clean and scalable so that work can easily be
  extended [# Project Structure](#project-structure)
- **Rapid Experimentation**: thanks to hydra command line superpowers | [# Your Superpowers](#your-superpowers)
- **Little Boilerplate**: thanks to automating pipelines with config instantiation | [# How It Works](#how-it-works)
- **Main Configs**: specify default training configuration | [# Main Config](#main-config)
- **Experiment Configs**: override chosen hyperparameters | [# Experiment Config](#experiment-config)
- **Workflow**: comes down to 4 simple steps | [# Workflow](#workflow)
- **Experiment Tracking**: Tensorboard, W&B, Neptune, Comet, MLFlow and CSVLogger
  | [# Experiment Tracking](#experiment-tracking)
- **Logs**: all logs (checkpoints, configs, etc.) are stored in a dynamically generated folder structure
  | [# Logs](#logs)
- **Hyperparameter Search**: made easier with Hydra plugins like Optuna Sweeper
  | [# Hyperparameter Search](#hyperparameter-search)
- **Tests**: generic, easy-to-adapt tests for speeding up the development | [# Tests](#tests)
- **Continuous Integration**: automatically test your repo with Github Actions
  | [# Continuous Integration](#continuous-integration)
- **Best Practices**: a couple of recommended tools, practices and standards | [# Best Practices](#best-practices)

<br>

## Project Structure

The directory structure of new project looks like this:

```
├── configs                   <- Hydra configuration files
│   ├── callbacks                <- Callbacks configs
│   ├── datamodule               <- Datamodule configs
│   ├── debug                    <- Debugging configs
│   ├── experiment               <- Experiment configs
│   ├── extras                   <- Extra utilities configs
│   ├── hparams_search           <- Hyperparameter search configs
│   ├── hydra                    <- Hydra configs
│   ├── local                    <- Local configs
│   ├── logger                   <- Logger configs
│   ├── model                    <- Model configs
│   ├── paths                    <- Project paths configs
│   ├── trainer                  <- Trainer configs
│   │
│   ├── eval.yaml             <- Main config for evaluation
│   └── train.yaml            <- Main config for training
│
├── data                   <- Project data
│
├── logs                   <- Logs generated by hydra and lightning loggers
│
├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials, and a short `-` delimited description,
│                             e.g. `1.0-jqp-initial-data-exploration.ipynb`.
│
├── scripts                <- Shell scripts
│
├── src                    <- Source code
│   ├── datamodules              <- Lightning datamodules
│   ├── models                   <- Lightning models
│   ├── utils                    <- Utility scripts
│   │
│   ├── eval.py                  <- Run evaluation
│   └── train.py                 <- Run training
│
├── tests                  <- Tests of any kind
│
├── .env.example              <- Example of file for storing private environment variables
├── .gitignore                <- List of files ignored by git
├── .pre-commit-config.yaml   <- Configuration of pre-commit hooks for code formatting
├── Makefile                  <- Makefile with commands like `make train` or `make test`
├── pyproject.toml            <- Configuration options for testing and linting
├── requirements.txt          <- File for installing python dependencies
├── setup.py                  <- File for installing project as a package
└── README.md
```

<br>

## How to run - train

Install dependencies

```bash
# clone project
git clone https://github.com/louisenaud/lightning-hydra-template-louise.git
cd lightning-hydra-template-louise

# [OPTIONAL] create conda environment
conda create -n myenv python=3.9
conda activate myenv

conda create -n py39 python=3.9.2
conda activate py39

# install pytorch according to instructions
# https://pytorch.org/get-started/

# install requirements
pip install -r requirements.txt
# or
poetry install
```

### Export requirements

```bash
poetry export -o requirements.txt --without-hashes --with dev
```

Train model with default configuration

```bash
# train on CPU
python src/train.py trainer=cpu

# train on GPU
python src/train.py trainer=gpu
```

Train model with chosen experiment configuration from [configs/experiment/](configs/experiment/)

```bash
python src/train.py experiment=experiment_name.yaml
python src/train.py experiment=mnist.yaml trainer=cpu
# on mac
python src/train.py experiment=mnist.yaml trainer=mps
```

You can override any parameter from command line like this

```bash
python src/train.py trainer.max_epochs=20 datamodule.batch_size=64
```

## Train using Docker

Run as Docker image

```bash
## Build Docker container image
make build

## Run the container with experiment=example.yaml
make run
```

## COG Inference

Install [COG](https://github.com/replicate/cog) (containers for Machine Learning)

```bash
sudo curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_`uname -s`_`uname -m`
sudo chmod +x /usr/local/bin/cog
```

Grab an image to test run the inference on

```bash
IMAGE_URL=https://gist.githubusercontent.com/bfirsh/3c2115692682ae260932a67d93fd94a8/raw/56b19f53f7643bb6c0b822c410c366c3a6244de2/mystery.jpg
curl $IMAGE_URL > input.jpg
```

Run inference

```bash
cog predict -i image=@input.jpg
```

returns top 5 predictions for the given input image

## Timm model

Train the model on any of models available on [timm library](https://github.com/rwightman/pytorch-image-models.git)
by passing thr model name as below

```bash
python src/train.py model.net.name="resnet18"
```

or you can also change the timm.yaml to configure for the model to be run

```bash
  _target_: src.models.timm_module.TimmModel
  name: "resnet18"
  num_classes: 10
```

## Demo App

Demo based on Gradio app can be run from the torch script checkpoint

```bash
#cifar10
python3 src/demo_cifar10_scripted.py -m ckpt_path=<path to model.script.pt>
#python -m src.demo_cifar10_scripted ckpt_path=logs/train/runs/2022-10-10_10-53-17/model.script.pt
#mnist
python3 src/demo_scripted.py -m ckpt_path=<path to model.script.pt>
#python3 src/demo_scripted.py -m ckpt_path=logs/train/runs/2022-10-10_10-25-21/model.script.pt

```

## Demo using Docker (Cifar10)

Docker
image: [vigneshbabuph/torchscript_gradio_demo](https://hub.docker.com/r/vigneshbabupj/torchscript_gradio_demo/tags)

Cd into the demo folder

```bash
cd /Docker/demo/

#Build image locally or pull from docker hub

#Buid image locally
#docker image build -t vigneshbabupj/torchscript_gradio_demo .

#pull from docker hub
docker pull vigneshbabupj/torchscript_gradio_demo:latest

#run demo from docker image
docker run --rm --volume `pwd`:/opt/src -it -p 8080:8080 vigneshbabupj/torchscript_gradio_demo:latest

```

place the model checkpoint to be used under the demo folder as "model.script.pt" or pass the ckpt_path as argument

Gradio server with the demo app is launched, click on the url to access and use it

<details>
<summary><b>Train with mixed precision</b></summary>

```bash
# train with pytorch native automatic mixed precision (AMP)
python train.py trainer=gpu +trainer.precision=16
```

</details>

<!-- deepspeed support still in beta
<details>
<summary><b>Optimize large scale models on multiple GPUs with Deepspeed</b></summary>

```bash
python train.py +trainer.
```

</details>
 -->

<details>
<summary><b>Train model with any logger available in PyTorch Lightning, like W&B or Tensorboard</b></summary>

```yaml
# set project and entity names in `configs/logger/wandb`
wandb:
  project: "your_project_name"
  entity: "your_wandb_team_name"
```

```bash
# train model with Weights&Biases (link to wandb dashboard should appear in the terminal)
python train.py logger=wandb
```

> **Note**: Lightning provides convenient integrations with most popular logging frameworks. Learn
> more [here](#experiment-tracking).

> **Note**: Using wandb requires you to [setup account](https://www.wandb.com/) first. After that just complete the
> config as below.

> **Note**: Click [here](https://wandb.ai/hobglob/template-dashboard/) to see example wandb dashboard generated with
> this template.

</details>

<details>
<summary><b>Train model with chosen experiment config</b></summary>

```bash
python train.py experiment=example
```

> **Note**: Experiment configs are placed in [configs/experiment/](configs/experiment/).

</details>

<details>
<summary><b>Attach some callbacks to run</b></summary>

```bash
python train.py callbacks=default
```

> **Note**: Callbacks can be used for things such as as model checkpointing, early stopping
> and [many more](https://pytorch-lightning.readthedocs.io/en/latest/extensions/callbacks.html#built-in-callbacks).

> **Note**: Callbacks configs are placed in [configs/callbacks/](configs/callbacks/).

</details>

<details>
<summary><b>Use different tricks available in Pytorch Lightning</b></summary>

```yaml
# gradient clipping may be enabled to avoid exploding gradients
python train.py +trainer.gradient_clip_val=0.5

  # run validation loop 4 times during a training epoch
python train.py +trainer.val_check_interval=0.25

  # accumulate gradients
python train.py +trainer.accumulate_grad_batches=10

  # terminate training after 12 hours
python train.py +trainer.max_time="00:12:00:00"
```

> **Note**: PyTorch Lightning provides
> about [40+ useful trainer flags](https://pytorch-lightning.readthedocs.io/en/latest/common/trainer.html#trainer-flags)
> .

</details>

<details>
<summary><b>Easily debug</b></summary>

```bash
# runs 1 epoch in default debugging mode
# changes logging directory to `logs/debugs/...`
# sets level of all command line loggers to 'DEBUG'
# enforces debug-friendly configuration
python train.py debug=default

# run 1 train, val and test loop, using only 1 batch
python train.py debug=fdr

# print execution time profiling
python train.py debug=profiler

# try overfitting to 1 batch
python train.py debug=overfit

# raise exception if there are any numerical anomalies in tensors, like NaN or +/-inf
python train.py +trainer.detect_anomaly=true

# log second gradient norm of the model
python train.py +trainer.track_grad_norm=2

# use only 20% of the data
python train.py +trainer.limit_train_batches=0.2 \
+trainer.limit_val_batches=0.2 +trainer.limit_test_batches=0.2
```

> **Note**: Visit [configs/debug/](configs/debug/) for different debugging configs.

</details>

<details>
<summary><b>Resume training from checkpoint</b></summary>

```yaml
python train.py ckpt_path="/path/to/ckpt/name.ckpt"
```

> **Note**: Checkpoint can be either path or URL.

> **Note**: Currently loading ckpt doesn't resume logger experiment, but it will be supported in future Lightning
> release.

</details>

<details>
<summary><b>Evaluate checkpoint on test dataset</b></summary>

```yaml
python eval.py ckpt_path="/path/to/ckpt/name.ckpt"
```

> **Note**: Checkpoint can be either path or URL.

</details>

<details>
<summary><b>Create a sweep over hyperparameters</b></summary>

```bash
# this will run 6 experiments one after the other,
# each with different combination of batch_size and learning rate
python train.py -m datamodule.batch_size=32,64,128 model.lr=0.001,0.0005
```

> **Note**: Hydra composes configs lazily at job launch time. If you change code or configs after launching a job/sweep,
> the final composed configs might be impacted.

</details>

<details>
<summary><b>Create a sweep over hyperparameters with Optuna</b></summary>

```bash
# this will run hyperparameter search defined in `configs/hparams_search/mnist_optuna.yaml`
# over chosen experiment config
python train.py -m hparams_search=mnist_optuna experiment=example
```

> **Note**: Using [Optuna Sweeper](https://hydra.cc/docs/next/plugins/optuna_sweeper) doesn't require you to add any
> boilerplate to your code, everything is defined in a [single config file](configs/hparams_search/mnist_optuna.yaml).

> **Warning**: Optuna sweeps are not failure-resistant (if one job crashes then the whole sweep crashes).

</details>

<details>
<summary><b>Execute all experiments from folder</b></summary>

```bash
python train.py -m 'experiment=glob(*)'
```

> **Note**: Hydra provides special syntax for controlling behavior of multiruns. Learn
> more [here](https://hydra.cc/docs/next/tutorials/basic/running_your_app/multi-run). The command above executes all
> experiments from [configs/experiment/](configs/experiment/).

</details>

<details>
<summary><b>Execute run for multiple different seeds</b></summary>

```bash
python train.py -m seed=1,2,3,4,5 trainer.deterministic=True logger=csv tags=["benchmark"]
```

> **Note**: `trainer.deterministic=True` makes pytorch more deterministic but impacts the performance.

</details>

<details>
<summary><b>Execute sweep on a remote AWS cluster</b></summary>

> **Note**: This should be achievable with simple config
> using [Ray AWS launcher for Hydra](https://hydra.cc/docs/next/plugins/ray_launcher). Example is not implemented in
> this
> template.

</details>

<!-- <details>
<summary><b>Execute sweep on a SLURM cluster</b></summary>

> This should be achievable with either [the right lightning trainer flags](https://pytorch-lightning.readthedocs.io/en/latest/clouds/cluster.html?highlight=SLURM#slurm-managed-cluster) or simple config using [Submitit launcher for Hydra](https://hydra.cc/docs/plugins/submitit_launcher). Example is not yet implemented in this template.

</details> -->

<details>
<summary><b>Use Hydra tab completion</b></summary>

> **Note**: Hydra allows you to autocomplete config argument overrides in shell as you write them, by pressing `tab`
> key. Read the [docs](https://hydra.cc/docs/tutorials/basic/running_your_app/tab_completion).

</details>

<details>
<summary><b>Apply pre-commit hooks</b></summary>

```bash
pre-commit run -a
```

> **Note**: Apply pre-commit hooks to do things like auto-formatting code and configs, performing code analysis or
> removing output from jupyter notebooks. See [# Best Practices](#best-practices) for more.

</details>

<details>
<summary><b>Run tests</b></summary>

```bash
# run all tests
pytest

# run tests from specific file
pytest tests/test_train.py

# run all tests except the ones marked as slow
pytest -k "not slow"
```

</details>

<details>
<summary><b>Use tags</b></summary>

Each experiment should be tagged in order to easily filter them across files or in logger UI:

```bash
python train.py tags=["mnist", "experiment_X"]
```

If no tags are provided, you will be asked to input them from command line:

```bash
>>> python train.py tags=[]
[2022-07-11 15:40:09,358][src.utils.utils][INFO] - Enforcing tags! <cfg.extras.enforce_tags=True>
[2022-07-11 15:40:09,359][src.utils.rich_utils][WARNING] - No tags provided in config. Prompting user to input tags...
Enter a list of comma separated tags (dev):
```

If no tags are provided for multirun, an error will be raised:

```bash
>>> python train.py -m +x=1,2,3 tags=[]
ValueError: Specify tags before launching a multirun!
```

> **Note**: Appending lists from command line is currently not supported in hydra :(

</details>

## How It Works

All PyTorch Lightning modules are dynamically instantiated from module paths specified in config. Example model config:

```yaml
_target_: src.models.mnist_model.MNISTLitModule
lr: 0.001
net:
  _target_: src.models.components.simple_dense_net.SimpleDenseNet
  input_size: 784
  lin1_size: 256
  lin2_size: 256
  lin3_size: 256
  output_size: 10
```

Using this config we can instantiate the object with the following line:

```python
model = hydra.utils.instantiate(config.model)
```

This allows you to easily iterate over new models! Every time you create a new one, just specify its module path and
parameters in appropriate config file. <br>

Switch between models and datamodules with command line arguments:

```bash
python train.py model=mnist
```

Example pipeline managing the instantiation logic: [src/train.py](src/train.py).

<br>

## Main Config

Location: [configs/train.yaml](configs/train.yaml) <br>
Main project config contains default training configuration.<br>
It determines how config is composed when simply executing command `python train.py`.<br>

<details>
<summary><b>Show main project config</b></summary>

```yaml
# order of defaults determines the order in which configs override each other
defaults:
  - _self_
  - datamodule: mnist.yaml
  - model: mnist.yaml
  - callbacks: default.yaml
  - logger: null # set logger here or use command line (e.g. `python train.py logger=csv`)
  - trainer: default.yaml
  - paths: default.yaml
  - extras: default.yaml
  - hydra: default.yaml

  # experiment configs allow for version control of specific hyperparameters
  # e.g. best hyperparameters for given model and datamodule
  - experiment: null

  # config for hyperparameter optimization
  - hparams_search: null

  # optional local config for machine/user specific settings
  # it's optional since it doesn't need to exist and is excluded from version control
  - optional local: default.yaml

  # debugging config (enable through command line, e.g. `python train.py debug=default)
  - debug: null

# task name, determines output directory path
task_name: "train"

# tags to help you identify your experiments
# you can overwrite this in experiment configs
# overwrite from command line with `python train.py tags="[first_tag, second_tag]"`
# appending lists from command line is currently not supported :(
# https://github.com/facebookresearch/hydra/issues/1547
tags: [ "dev" ]

# set False to skip model training
train: True

# evaluate on test set, using best model weights achieved during training
# lightning chooses best weights based on the metric specified in checkpoint callback
test: True

# simply provide checkpoint path to resume training
ckpt_path: null

# seed for random number generators in pytorch, numpy and python.random
seed: null
```

</details>

<br>

## Experiment Config

Location: [configs/experiment](configs/experiment)<br>
Experiment configs allow you to overwrite parameters from main config.<br>
For example, you can use them to version control best hyperparameters for each combination of model and dataset.

<details>
<summary><b>Show example experiment config</b></summary>

```yaml
# @package _global_

# to execute this experiment run:
# python train.py experiment=example

defaults:
  - override /datamodule: mnist.yaml
  - override /model: mnist.yaml
  - override /callbacks: default.yaml
  - override /trainer: default.yaml

# all parameters below will be merged with parameters from default configurations set above
# this allows you to overwrite only specified parameters

tags: [ "mnist", "simple_dense_net" ]

seed: 12345

trainer:
  min_epochs: 10
  max_epochs: 10
  gradient_clip_val: 0.5

model:
  optimizer:
    lr: 0.002
  net:
    lin1_size: 128
    lin2_size: 256
    lin3_size: 64

datamodule:
  batch_size: 64

logger:
  wandb:
    tags: ${tags}
    group: "mnist"
```

</details>

<br>

## Workflow

**Basic workflow**

1. Write your PyTorch Lightning module (see [models/mnist_module.py](src/models/mnist_module.py) for example)
2. Write your PyTorch Lightning datamodule (see [datamodules/mnist_datamodule.py](src/datamodules/mnist_datamodule.py)
   for example)
3. Write your experiment config, containing paths to model and datamodule
4. Run training with chosen experiment config:
   ```bash
   python src/train.py experiment=experiment_name.yaml
   ```

**Experiment design**

_Say you want to execute many runs to plot how accuracy changes in respect to batch size._

1. Execute the runs with some config parameter that allows you to identify them easily, like tags:

   ```bash
   python train.py -m logger=csv datamodule.batch_size=16,32,64,128 tags=["batch_size_exp"]
   ```

2. Write a script or notebook that searches over the `logs/` folder and retrieves csv logs from runs containing given
   tags in config. Plot the results.

<br>

## Logs

Hydra creates new output directory for every executed run.

Default logging structure:

```
├── logs
│   ├── task_name
│   │   ├── runs                        # Logs generated by single runs
│   │   │   ├── YYYY-MM-DD_HH-MM-SS       # Datetime of the run
│   │   │   │   ├── .hydra                  # Hydra logs
│   │   │   │   ├── csv                     # Csv logs
│   │   │   │   ├── wandb                   # Weights&Biases logs
│   │   │   │   ├── checkpoints             # Training checkpoints
│   │   │   │   └── ...                     # Any other thing saved during training
│   │   │   └── ...
│   │   │
│   │   └── multiruns                   # Logs generated by multiruns
│   │       ├── YYYY-MM-DD_HH-MM-SS       # Datetime of the multirun
│   │       │   ├──1                        # Multirun job number
│   │       │   ├──2
│   │       │   └── ...
│   │       └── ...
│   │
│   └── debugs                          # Logs generated when debugging config is attached
│       └── ...
```

</details>

You can change this structure by modifying paths in [hydra configuration](configs/hydra).

<br>

## Experiment Tracking

PyTorch Lightning supports many popular logging frameworks: [Weights&Biases](https://www.wandb.com/)
, [Neptune](https://neptune.ai/), [Comet](https://www.comet.ml/), [MLFlow](https://mlflow.org)
, [Tensorboard](https://www.tensorflow.org/tensorboard/).

These tools help you keep track of hyperparameters and output metrics and allow you to compare and visualize results. To
use one of them simply complete its configuration in [configs/logger](configs/logger) and run:

```bash
python train.py logger=logger_name
```

You can use many of them at once (see [configs/logger/many_loggers.yaml](configs/logger/many_loggers.yaml) for example).

You can also write your own logger.

Lightning provides convenient method for logging custom metrics from inside LightningModule. Read
the [docs](https://pytorch-lightning.readthedocs.io/en/latest/extensions/logging.html#automatic-logging) or take a look
at [MNIST example](src/models/mnist_module.py).

<br>

## Tests

Template comes with generic tests implemented with `pytest`.

```bash
# run all tests
pytest

# run tests from specific file
pytest tests/test_train.py

# run all tests except the ones marked as slow
pytest -k "not slow"
```

Most of the implemented tests don't check for any specific output - they exist to simply verify that executing some
commands doesn't end up in throwing exceptions. You can execute them once in a while to speed up the development.

Currently, the tests cover cases like:

- running 1 train, val and test step
- running 1 epoch on 1% of data, saving ckpt and resuming for the second epoch
- running 2 epochs on 1% of data, with DDP simulated on CPU

And many others. You should be able to modify them easily for your use case.

There is also `@RunIf` decorator implemented, that allows you to run tests only if certain conditions are met, e.g. GPU
is available or system is not windows. See the [examples](tests/test_train.py).

<br>

## Hyperparameter Search

You can define hyperparameter search by adding new config file to [configs/hparams_search](configs/hparams_search).

<details>
<summary><b>Show example hyperparameter search config</b></summary>

```yaml
# @package _global_

defaults:
  - override /hydra/sweeper: optuna

# choose metric which will be optimized by Optuna
# make sure this is the correct name of some metric logged in lightning module!
optimized_metric: "val/acc_best"

# here we define Optuna hyperparameter search
# it optimizes for value returned from function with @hydra.main decorator
hydra:
  sweeper:
    _target_: hydra_plugins.hydra_optuna_sweeper.optuna_sweeper.OptunaSweeper

    # 'minimize' or 'maximize' the objective
    direction: maximize

    # total number of runs that will be executed
    n_trials: 20

    # choose Optuna hyperparameter sampler
    # docs: https://optuna.readthedocs.io/en/stable/reference/samplers.html
    sampler:
      _target_: optuna.samplers.TPESampler
      seed: 1234
      n_startup_trials: 10 # number of random sampling runs before optimization starts

    # define hyperparameter search space
    params:
      model.optimizer.lr: interval(0.0001, 0.1)
      datamodule.batch_size: choice(32, 64, 128, 256)
      model.net.lin1_size: choice(64, 128, 256)
      model.net.lin2_size: choice(64, 128, 256)
      model.net.lin3_size: choice(32, 64, 128, 256)
```

</details>

Next, execute it with: `python train.py -m hparams_search=mnist_optuna`

Using this approach doesn't require adding any boilerplate to code, everything is defined in a single config file. The
only necessary thing is to return the optimized metric value from the launch file.

You can use different optimization frameworks integrated with Hydra,
like [Optuna, Ax or Nevergrad](https://hydra.cc/docs/plugins/optuna_sweeper/).

The `optimization_results.yaml` will be available under `logs/task_name/multirun` folder.

This approach doesn't support advanced techniques like prunning - for more sophisticated search, you should probably
write a dedicated optimization task (without multirun feature).

<br>

## Continuous Integration

Template comes with CI workflows implemented in Github Actions:

- `.github/workflows/test.yaml`: running all tests with pytest
- `.github/workflows/code-quality-main.yaml`: running pre-commits on main branch for all files
- `.github/workflows/code-quality-pr.yaml`: running pre-commits on pull requests for modified files only

> **Note**: You need to enable the GitHub Actions from the settings in your repository.

<br>

## Distributed Training

Lightning supports multiple ways of doing distributed training. The most common one is DDP, which spawns separate
process for each GPU and averages gradients between them. To learn about other approaches read
the [lightning docs](https://pytorch-lightning.readthedocs.io/en/latest/advanced/multi_gpu.html).

You can run DDP on mnist example with 4 GPUs like this:

```bash
python train.py trainer=ddp
```

> **Note**: When using DDP you have to be careful how you write your models - read
> the [docs](https://pytorch-lightning.readthedocs.io/en/latest/advanced/multi_gpu.html).

<br>

## Accessing Datamodule Attributes In Model

The simplest way is to pass datamodule attribute directly to model on initialization:

```python
# ./src/train.py
datamodule = hydra.utils.instantiate(config.datamodule)
model = hydra.utils.instantiate(config.model, some_param=datamodule.some_param)
```

> **Note**: Not a very robust solution, since it assumes all your datamodules have `some_param` attribute available.

Similarly, you can pass a whole datamodule config as an init parameter:

```python
# ./src/train.py
model = hydra.utils.instantiate(config.model, dm_conf=config.datamodule, _recursive_=False)
```

You can also pass a datamodule config parameter to your model through variable interpolation:

```yaml
# ./configs/model/my_model.yaml
_target_: src.models.my_module.MyLitModule
lr: 0.01
some_param: ${datamodule.some_param}
```

Another approach is to access datamodule in LightningModule directly through Trainer:

```python
# ./src/models/mnist_module.py
def on_train_start(self):
    self.some_param = self.trainer.datamodule.some_param
```

> **Note**: This only works after the training starts since otherwise trainer won't be yet available in LightningModule.

<br>

## Best Practices

<details>
<summary><b>Use Miniconda for GPU environments</b></summary>

Use miniconda for your python environments (it's usually unnecessary to install full anaconda environment, miniconda
should be enough).
It makes it easier to install some dependencies, like cudatoolkit for GPU support. It also allows you to access your
environments globally.

Example installation:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Create new conda environment:

```bash
conda create -n myenv python=3.8
conda activate myenv
```

</details>

<details>
<summary><b>Use automatic code formatting</b></summary>

Use pre-commit hooks to standardize code formatting of your project and save mental energy.<br>
Simply install pre-commit package with:

```bash
pip install pre-commit
```

Next, install hooks from [.pre-commit-config.yaml](.pre-commit-config.yaml):

```bash
pre-commit install
```

After that your code will be automatically reformatted on every new commit.

Currently template contains configurations of:

- **black** (python code formatting)
- **isort** (python import sorting)
- **pyupgrade** (upgrading python syntax to newer version)
- **docformatter** (python docstring formatting)
- **flake8** (python pep8 code analysis)
- **prettier** (yaml formatting)
- **nbstripout** (clearing output from jupyter notebooks)
- **bandit** (python security linter)
- **mdformat** (markdown formatting)
- **codespell** (word spellling linter)

To reformat all files in the project use command:

```bash
pre-commit run -a
```

</details>

<details>
<summary><b>Set private environment variables in .env file</b></summary>

System specific variables (e.g. absolute paths to datasets) should not be under version control or it will result in
conflict between different users. Your private keys also shouldn't be versioned since you don't want them to be
leaked.<br>

Template contains `.env.example` file, which serves as an example. Create a new file called `.env` (this name is
excluded from version control in .gitignore).
You should use it for storing environment variables like this:

```
MY_VAR=/home/user/my_system_path
```

All variables from `.env` are loaded in `train.py` automatically.

Hydra allows you to reference any env variable in `.yaml` configs like this:

```yaml
path_to_data: ${oc.env:MY_VAR}
```

</details>

<details>
<summary><b>Name metrics using '/' character</b></summary>

Depending on which logger you're using, it's often useful to define metric name with `/` character:

```python
self.log("train/loss", loss)
```

This way loggers will treat your metrics as belonging to different sections, which helps to get them organised in UI.

</details>

<details>
<summary><b>Use torchmetrics</b></summary>

Use official [torchmetrics](https://github.com/PytorchLightning/metrics) library to ensure proper calculation of
metrics. This is especially important for multi-GPU training!

For example, instead of calculating accuracy by yourself, you should use the provided `Accuracy` class like this:

```python
from torchmetrics.classification.accuracy import Accuracy


class LitModel(LightningModule):
    def __init__(self)
        self.train_acc = Accuracy()
        self.val_acc = Accuracy()

    def training_step(self, batch, batch_idx):
        ...
        acc = self.train_acc(predictions, targets)
        self.log("train/acc", acc)
        ...

    def validation_step(self, batch, batch_idx):
        ...
        acc = self.val_acc(predictions, targets)
        self.log("val/acc", acc)
        ...
```

Make sure to use different metric instance for each step to ensure proper value reduction over all GPU processes.

Torchmetrics provides metrics for most use cases, like F1 score or confusion matrix.
Read [documentation](https://torchmetrics.readthedocs.io/en/latest/#more-reading) for more.

</details>

<details>
<summary><b>Follow PyTorch Lightning style guide</b></summary>

The style guide is available [here](https://pytorch-lightning.readthedocs.io/en/latest/starter/style_guide.html).<br>

1. Be explicit in your init. Try to define all the relevant defaults so that the user doesn’t have to guess. Provide
   type hints. This way your module is reusable across projects!

   ```python
   class LitModel(LightningModule):
       def __init__(self, layer_size: int = 256, lr: float = 0.001):
   ```

2. Preserve the recommended method order.

   ```python
   class LitModel(LightningModule):

       def __init__():
           ...

       def forward():
           ...

       def training_step():
           ...

       def training_step_end():
           ...

       def training_epoch_end():
           ...

       def validation_step():
           ...

       def validation_step_end():
           ...

       def validation_epoch_end():
           ...

       def test_step():
           ...

       def test_step_end():
           ...

       def test_epoch_end():
           ...

       def configure_optimizers():
           ...

       def any_extra_hook():
           ...
   ```

</details>

<details>
<summary><b>Version control your data and models with DVC</b></summary>

Use [DVC](https://dvc.org) to version control big files, like your data or trained ML models.<br>
To initialize the dvc repository:

```bash
dvc init
```

To start tracking a file or directory, use `dvc add`:

```bash
dvc add data/MNIST
```

DVC stores information about the added file (or a directory) in a special .dvc file named data/MNIST.dvc, a small text
file with a human-readable format. This file can be easily versioned like source code with Git, as a placeholder for the
original data:

```bash
git add data/MNIST.dvc data/.gitignore
git commit -m "Add raw data"
```

</details>

<details>
<summary><b>Support installing project as a package</b></summary>

It allows other people to easily use your modules in their own projects.
Change name of the `src` folder to your project name and complete the `setup.py` file.

Now your project can be installed from local files:

```bash
pip install -e .
```

Or directly from git repository:

```bash
pip install git+git://github.com/YourGithubName/your-repo-name.git --upgrade
```

So any file can be easily imported into any other file like so:

```python
from project_name.models.mnist_module import MNISTLitModule
from project_name.datamodules.mnist_datamodule import MNISTDataModule
```

</details>

<details>
<summary><b>Keep local configs out of code versioning</b></summary>

Some configurations are user/machine/installation specific (e.g. configuration of local cluster, or harddrive paths on a
specific machine). For such scenarios, a file [configs/local/default.yaml](configs/local/) can be created which is
automatically loaded but not tracked by Git.

Example SLURM cluster config:

```yaml
# @package _global_

defaults:
  - override /hydra/launcher@_here_: submitit_slurm

data_dir: /mnt/scratch/data/

hydra:
  launcher:
    timeout_min: 1440
    gpus_per_task: 1
    gres: gpu:1
  job:
    env_set:
      MY_VAR: /home/user/my/system/path
      MY_KEY: asdgjhawi8y23ihsghsueity23ihwd
```

</details>

<br>

## Reference repos

This template was inspired by:

- [aiplaybookin/lightning-hydra-template](https://github.com/aiplaybookin/lightning-hydra-template)
- [ashleve/lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template)
- [vigneshbabupj/lightning-hydra-timm-template](https://github.com/vigneshbabupj/lightning-hydra-timm-template)
- [hppRC/template-pytorch-lightning-hydra-mlflow-poetry](https://github.com/hppRC/template-pytorch-lightning-hydra-mlflow-poetry)
- [PyTorchLightning/deep-learninig-project-template](https://github.com/PyTorchLightning/deep-learning-project-template)
- [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
- [lucmos/nn-template](https://github.com/lucmos/nn-template)
- [grok-ai/nn-template-core](https://github.com/grok-ai/nn-template-core)
- [kedro-org/kedro](https://github.com/kedro-org/kedro)

Useful repositories:

- [pytorch/hydra-torch](https://github.com/pytorch/hydra-torch) - safely configuring PyTorch classes with Hydra
- [romesco/hydra-lightning](https://github.com/romesco/hydra-lightning) - safely configuring PyTorch Lightning classes
  with Hydra
- [PyTorchLightning/lightning-transformers](https://github.com/PyTorchLightning/lightning-transformers) - official
  Lightning Transformers repo built with Hydra

Other resources:

- [Cookiecutter Data Science Project Structure Opinions](http://drivendata.github.io/cookiecutter-data-science/#opinions)
- [The Machine Learning Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf)
