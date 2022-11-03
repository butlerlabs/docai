"""
This file contains utility functions for working with bounding boxes
and converting them into formats needed for different ML models.
"""

from docai.generated.models.bounding_box_dto import BoundingBoxDto


def butler_bbx_to_min_max(butler_bbx: BoundingBoxDto):
    """
    Converts a bounding box in the format used by Butler into the following format:
    [x_min, y_min, x_max, y_max]

    NOTE: the top left point of the coordinate system is (0, 0)
    """
    width = butler_bbx.width
    height = butler_bbx.height
    top = butler_bbx.top
    left = butler_bbx.left

    return [left, top, left + width, top + height]
