"""
Will store all functions needed to generate the shape(path) layer in lottie
"""

import sys
import settings
from misc import Count
from properties.shape import gen_properties_shape
from properties.shapeKeyframed import gen_properties_shapeKeyframed
sys.path.append("..")


def gen_shapes_shape(lottie, layer, idx):
    """
    Generates the dictionary corresponding to shapes/shape.json

    Args:
        lottie (dict)               : The lottie generated shape layer will be stored in it
        layer  (lxml.etree._Element): Synfig format shape(list of bline points) layer
        idx    (int)                : Stores the index of the shape layer

    Returns:
        (None)
    """
    index = Count()
    lottie["ty"] = "sh"     # Type: shape
    lottie["ix"] = idx      # Index
    lottie["ks"] = {}
    for child in layer:
        if child.tag == "param":
            if child.attrib["name"] == "bline":
                bline_point = child[0]
                gen_properties_shapeKeyframed(lottie["ks"], bline_point, index.inc())
