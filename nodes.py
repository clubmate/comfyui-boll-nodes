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

class RemoveLastImage:
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

class WANConfig:
    CATEGORY = "config"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (["480p", "720p", "1080p"], {"default": "480p"}),
                "video_length": ("INT", {"default": 81, "min": 1, "max": 81}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 100}),
                "model_float": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 10.0}),
                "cfg": ("FLOAT", {"default": 3.5, "min": 1.0, "max": 20.0}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "FLOAT", "FLOAT")
    RETURN_NAMES = ("width", "height", "video_length", "steps", "model_float", "cfg")
    FUNCTION = "execute"

    def execute(self, resolution, video_length, steps, model_float, cfg):
        if resolution == "480p":
            width, height = 854, 480
        elif resolution == "720p":
            width, height = 1280, 720
        elif resolution == "1080p":
            width, height = 1920, 1080
        else:
            width, height = 1280, 720  # Fallback
        return (width, height, video_length, steps, model_float, cfg)