import hydra
from omegaconf import DictConfig, OmegaConf

import  pyalgo.internal.biz.prometheus.flask_web


@hydra.main(version_base=None, config_path="../config", config_name="config")
def start_process(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    start_process()