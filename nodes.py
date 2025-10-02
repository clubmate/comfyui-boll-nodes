import torch

class GetLastImage:
    CATEGORY = "image/batch"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    def execute(self, images):
        # images is a tensor of shape (batch, height, width, channels)
        # Get the last image and add batch dimension back
        last_image = images[-1].unsqueeze(0)
        return (last_image,)

class DeleteLastImage:
    CATEGORY = "image/batch"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    def execute(self, images):
        # images is a tensor of shape (batch, height, width, channels)
        # Remove the last image from the batch
        remaining_images = images[:-1]
        return (remaining_images,)