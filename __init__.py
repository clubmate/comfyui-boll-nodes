from .nodes import GetLastImage, RemoveLastImage, WANConfig

NODE_CLASS_MAPPINGS = {
    "GetLastImage": GetLastImage,
    "RemoveLastImage": RemoveLastImage,
    "WANConfig": WANConfig,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GetLastImage": "Get Last Image",
    "RemoveLastImage": "Remove Last Image",
    "WANConfig": "WAN Config",
}