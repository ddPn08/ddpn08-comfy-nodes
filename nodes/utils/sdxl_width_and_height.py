MAX_RESOLUTION = 8192


class SDXLWidthAndHeight:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": (
                    "INT",
                    {"default": 512, "min": 64, "max": MAX_RESOLUTION, "step": 8},
                ),
                "height": (
                    "INT",
                    {"default": 512, "min": 64, "max": MAX_RESOLUTION, "step": 8},
                ),
                "multiplier": (
                    "INT",
                    {"default": 4, "min": 1, "max": 8, "step": 1},
                ),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    FUNCTION = "convert"

    CATEGORY = "ddpn08/utils"

    def convert(self, width, height, multiplier):
        return (
            int(width),
            int(height),
            int(width * multiplier),
            int(height * multiplier),
        )
