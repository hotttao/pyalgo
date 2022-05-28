import imp
import hydra
from omegaconf import DictConfig, OmegaConf

from pyalgo.internal.biz.prometheus import flask_web
from pyalgo.internal.biz.prometheus import multiprocess_client


@hydra.main(version_base=None, config_path="../config", config_name="config")
def start_process(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    # flask_web.app.run()
    multiprocess_client.main()


if __name__ == "__main__":
    start_process()