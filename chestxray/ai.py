print("Importing libraries...")
from . import exceptions

from typing import Optional

import torch
import torchxrayvision as xray
from skimage.io import imread
from torchvision.transforms import Compose


class XrayScanner:
    def __init__(self, weights: Optional[str] = "all") -> None:
        """
        Runs a neural network from a pretrained model.

        Note: This does not use GPU Acceleration currently.

        Args:
            weights: Pre trained weights to use. Defaults to "all".
        """

        print("Loading model...")
        self.model = xray.models.DenseNet(weights=weights)

    def scan_xray(self, image_path: str) -> None:
        """
        Scans an image using the model which was loaded.

        Args:
            image_path: Path to the image. Ideally should be absolute.
        """
        print("Opening image...")
        image = imread(image_path)
        image = xray.datasets.normalize(image, 255)

        print("Running image correction...")
        if len(image.shape) < 2:
            raise exceptions.InvalidDimensions("Dimensions is lower than 2.")
            return

        elif len(image.shape) > 2:
            image = image[:, :, 0]

        image = image[None, :, :]  # Add color channel
        image = Compose(
            [xray.datasets.XRayCenterCrop(), xray.datasets.XRayResizer(224)]
        )(image)

        print("Predicting abnormalities...")
        with torch.no_grad():
            image = torch.from_numpy(image).unsqueeze(0)
            prediction = self.model(image).cpu()
            prediction = dict(zip(
                xray.datasets.default_pathologies,
                prediction[0].detach().numpy())
            )
            return prediction
