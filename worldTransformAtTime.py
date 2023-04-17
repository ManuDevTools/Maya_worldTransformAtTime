"""
Functions to get in Maya, the world position, rotation and scale of an object at a given moment in time.
"""

import math
from maya import cmds
import maya.api.OpenMaya as om


def getLocationAtTime(node, time) -> om.MVector:
    """Returns a MVector with world X, Y, Z translation"""
    worldMatrix = om.MMatrix(cmds.getAttr(f'{node}.worldMatrix', time = time))
    transformationMatrix = om.MTransformationMatrix(worldMatrix)

    return transformationMatrix.translation(om.MSpace.kWorld)


def getRotationAtTime(node, time) -> om.MVector:
    """Returns a MVector with world X, Y, Z rotation"""
    worldMatrix = om.MMatrix(cmds.getAttr(f'{node}.worldMatrix', time = time))
    transformationMatrix = om.MTransformationMatrix(worldMatrix)

    rotation = transformationMatrix.rotation(asQuaternion=False)
    rotationDegreesVector = om.MVector([math.degrees(rotation.x), math.degrees(rotation.y), math.degrees(rotation.z)])

    return rotationDegreesVector  


def getScaleAtTime(node, time) -> om.MVector:
    """Returns a MVector with world X, Y, Z scale"""
    worldMatrix = om.MMatrix(cmds.getAttr(f'{node}.worldMatrix', time = time))
    transformationMatrix = om.MTransformationMatrix(worldMatrix)

    return transformationMatrix.scale(om.MSpace.kWorld)
