from kymjtfs.cnn import MedleySolosClassifier, MedleyDataModule

import pytorch_lightning as pl, fire

from pytorch_lightning import Trainer
from pytorch_lightning.callbacks.early_stopping import EarlyStopping


def run_train(n_epochs = 200, batch_size = 4):
    early_stop_callback = EarlyStopping(monitor="val/loss", 
                                        min_delta=0.00, 
                                        patience=3, 
                                        verbose=False, 
                                        mode="max")
    trainer = pl.Trainer(gpus=-1, 
                        max_epochs=n_epochs,
                        progress_bar_refresh_rate=1, 
                        checkpoint_callback=True,
                        callbacks=[early_stop_callback])
    model, dataset = MedleySolosClassifier(), MedleyDataModule(batch_size=batch_size) 
    trainer.fit(model, dataset)
    trainer.test(model, dataset)


def main():
  fire.Fire(run_train)


if __name__ == "__main__":
    main()