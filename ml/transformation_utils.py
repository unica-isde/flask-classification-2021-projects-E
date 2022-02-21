import os
import torchvision.utils
from torchvision import transforms
from datetime import datetime

from ml.classification_utils import fetch_image

from config import Configuration
conf = Configuration()


def jitter_transformation(img_id: str,
                          brightness: float = 1,
                          contrast: float = 1,
                          saturation: float = 1,
                          hue: float = 0.5):
    """Returns the location of the jittered image.

    :param str img_id: the id of the image to which apply the random jitter
    :param float brightness: brightness value for the jitter (non negative)
    :param float contrast: contrast value for the jitter (non negative)
    :param float saturation: saturation value for the jitter (non negative)
    :param float hue: hue value for the jitter (0 &lt= hue  &lt= 0.5)

    :return: the name of the jittered image stored in predefined folder for transformed images
    """
    img = fetch_image(img_id)
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.ColorJitter(
                brightness,
                contrast,
                saturation,
                hue
            )
        ]
    )

    # apply transform from torchvision
    img = img.convert('RGB')
    preprocessed = transform(img)
    img.close()

    # current date and time
    now = datetime.now()
    now_formatted = now.strftime("%m%d%Y%H%M%S")

    # generate image name and output path
    image_name = "{}_{}.jpeg".format(img_id.replace('.JPEG', ''), now_formatted)
    output_path = os.path.join(conf.transformed_images_folder_path, image_name)

    # check if the "transformed_images" folder exists
    if not os.path.exists(conf.transformed_images_folder_path):
        os.mkdir(conf.transformed_images_folder_path)

    torchvision.utils.save_image(preprocessed, fp=output_path)

    return image_name
