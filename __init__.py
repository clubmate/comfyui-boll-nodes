from .nodes import GetLastImage, DeleteLastImage

NODE_CLASS_MAPPINGS = {
    "GetLastImage": GetLastImage,
    "DeleteLastImage": DeleteLastImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GetLastImage": "Get Last Image",
    "DeleteLastImage": "Delete Last Image",
}