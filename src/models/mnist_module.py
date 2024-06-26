from typing import Any, List, Literal

import torch
from pytorch_lightning import LightningModule
from torchmetrics import MaxMetric, MeanMetric
from torchmetrics.classification.accuracy import Accuracy
from torchvision import transforms as T


class MNISTLitModule(LightningModule):
    """Example of LightningModule for MNIST classification.

    A LightningModule organizes your PyTorch code into 6 sections:
        - Computations (init)
        - Train loop (training_step)
        - Validation loop (validation_step)
        - Test loop (test_step)
        - Prediction Loop (predict_step)
        - Optimizers and LR Schedulers (configure_optimizers)

    Docs:
        https://pytorch-lightning.readthedocs.io/en/latest/common/lightning_module.html
    """

    def __init__(
        self,
        net: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        task: Literal["binary", "multiclass", "multilabel"] = "multiclass",
        n_classes: int = 10,
    ):
        super().__init__()

        # this line allows to access init params with 'self.hparams' attribute
        # also ensures init params will be stored in ckpt
        self.save_hyperparameters(logger=False, ignore=["net"])

        self.net = net

        # loss function
        self.criterion = torch.nn.CrossEntropyLoss()

        # metric objects for calculating and averaging accuracy across batches
        self.train_acc = Accuracy(task=task, num_classes=n_classes)
        self.val_acc = Accuracy(task=task, num_classes=n_classes)
        self.test_acc = Accuracy(task=task, num_classes=n_classes)

        # for averaging loss across batches
        self.train_loss = MeanMetric()
        self.val_loss = MeanMetric()
        self.test_loss = MeanMetric()

        # for tracking best so far validation accuracy
        self.val_acc_best = MaxMetric()

        self.predict_transform = T.Normalize((0.1307,), (0.3081,))
        # store outputs
        self.training_step_outputs = []  # save outputs in each batch to compute metric overall epoch
        self.training_step_targets = []  # save targets in each batch to compute metric overall epoch
        self.val_step_outputs = []  # save outputs in each batch to compute metric overall epoch
        self.val_step_targets = []  # save targets in each batch to compute metric overall epoch

    def forward(self, x: torch.Tensor):
        return self.net(x)

    @torch.jit.export
    def forward_jit(self, x: torch.Tensor):
        with torch.no_grad():
            # transform the inputs
            x = self.predict_transform(x)

            # forward pass
            logits = self(x)

            preds = torch.nn.functional.softmax(logits, dim=-1)

        return preds

    def on_train_start(self):
        # by default lightning executes validation step sanity checks before training starts,
        # so we need to make sure val_acc_best doesn't store accuracy from these checks
        self.val_acc_best.reset()

    def step(self, batch: Any):
        x, y = batch
        logits = self.forward(x)
        loss = self.criterion(logits, y)
        preds = torch.argmax(logits, dim=1)
        return loss, preds, y

    def training_step(self, batch: Any, batch_idx: int):
        loss, preds, targets = self.step(batch)

        # update and log metrics
        self.train_loss(loss)
        self.train_acc(preds, targets)
        self.log("train/loss", self.train_loss, on_step=False, on_epoch=True, prog_bar=True)
        self.log("train/acc", self.train_acc, on_step=False, on_epoch=True, prog_bar=True)
        #
        # # storing targets and predictions for metrics
        # y_pred = preds.argmax(dim=1).cpu().numpy()
        # y_true = targets.cpu().numpy()
        self.training_step_outputs.extend(preds)
        self.training_step_targets.extend(targets)

        # we can return here dict with any tensors
        # and then read it in some callback or in `training_epoch_end()` below
        # remember to always return loss from `training_step()` or backpropagation will fail!
        return {"loss": loss, "preds": preds, "targets": targets}

    def on_train_epoch_end(self):
        # `outputs` is a list of dicts returned from `training_step()`
        # free up the memory
        # --> HERE STEP 3 <--
        self.training_step_outputs.clear()
        self.training_step_targets.clear()

    def validation_step(self, batch: Any, batch_idx: int):
        loss, preds, targets = self.step(batch)

        # update and log metrics
        self.val_loss(loss)
        self.val_acc(preds, targets)
        self.log("val/loss", self.val_loss, on_step=False, on_epoch=True, prog_bar=True)
        self.log("val/acc", self.val_acc, on_step=False, on_epoch=True, prog_bar=True)

        # storing results
        self.val_step_outputs.extend(preds)
        self.val_step_targets.extend(targets)

        return {"loss": loss, "preds": preds, "targets": targets}

    def on_validation_epoch_end(self):
        val_all_outputs = torch.tensor(self.val_step_outputs)
        val_all_targets = torch.tensor(self.val_step_targets)
        acc = self.val_acc(val_all_outputs, val_all_targets)  # get current val acc
        self.val_acc_best(acc)  # update best so far val acc
        # log `val_acc_best` as a value through `.compute()` method, instead of as a metric object
        # otherwise metric would be reset by lightning after each epoch
        self.log("val/acc_best", self.val_acc_best.compute(), prog_bar=True)

    def test_step(self, batch: Any, batch_idx: int):
        loss, preds, targets = self.step(batch)

        # update and log metrics
        self.test_loss(loss)
        self.test_acc(preds, targets)
        self.log("test/loss", self.test_loss, on_step=False, on_epoch=True, prog_bar=True)
        self.log("test/acc", self.test_acc, on_step=False, on_epoch=True, prog_bar=True)

        return {"loss": loss, "preds": preds, "targets": targets}

    def on_test_epoch_end(self):
        pass

    def configure_optimizers(self):
        """Choose what optimizers and learning-rate schedulers to use in your optimization.
        Normally you'd need one. But in the case of GANs or similar you might have multiple.

        Examples:
            https://pytorch-lightning.readthedocs.io/en/latest/common/lightning_module.html#configure-optimizers
        """
        return {
            "optimizer": self.hparams.optimizer(params=self.parameters()),
        }


if __name__ == "__main__":
    import hydra
    import omegaconf
    import pyrootutils

    root = pyrootutils.setup_root(__file__, pythonpath=True)
    cfg = omegaconf.OmegaConf.load(root / "configs" / "model" / "mnist.yaml")
    _ = hydra.utils.instantiate(cfg)
