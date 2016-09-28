# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named lp_fakeDefocusExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from lp_fakeDefocusExt import *
except ImportError:
    pass

def getPluginID():
    return "lp_fakeDefocus"

def getLabel():
    return "lp_fakeDefocus"

def getVersion():
    return 1

def getGrouping():
    return "Filter"

def getPluginDescription():
    return "A very fake defocus-effect. Tries to mimic classic bokeh-aesthetics, which can work to an extend."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.userNatron = lastNode.createPageParam("userNatron", "Controls")
    param = lastNode.createDoubleParam("defocussize", "size")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("adjust the \'defocus\' size")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.defocussize = param
    del param

    param = lastNode.createDoubleParam("aspect", "aspect ratio")
    param.setMinimum(0.1, 0)
    param.setMaximum(2, 0)
    param.setDisplayMinimum(0.1, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("sets the aspect ratio for the bokeh (e.g. for anamorphic shots)")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.aspect = param
    del param

    param = lastNode.createStringParam("copyright", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("lp_fakeDefocus v1.0\n(c) 2016 by lucas pfaff")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.copyright = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['userNatron', 'Node', 'Settings', 'Info'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output1")
    lastNode.setLabel("Output1")
    lastNode.setPosition(2787, 420)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "img"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("img")
    lastNode.setLabel("img")
    lastNode.setPosition(2787, -5)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupimg = lastNode

    del lastNode
    # End of node "img"

    # Start of node "ErodeSmooth1"
    lastNode = app.createNode("net.sf.cimg.CImgErodeSmooth", 2, group)
    lastNode.setScriptName("ErodeSmooth1")
    lastNode.setLabel("ErodeSmooth1")
    lastNode.setPosition(2787, 210)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupErodeSmooth1 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("exponent")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("Gaussian")
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "ErodeSmooth1"

    # Start of node "Transform1"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform1")
    lastNode.setLabel("Transform1")
    lastNode.setPosition(2787, 99)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform1 = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Transform1"

    # Start of node "Transform1_2"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Transform1_2")
    lastNode.setLabel("Transform1_2")
    lastNode.setPosition(2787, 319)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupTransform1_2 = lastNode

    param = lastNode.getParam("scale")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Transform1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupTransform1_2)
    groupErodeSmooth1.connectInput(0, groupTransform1)
    groupTransform1.connectInput(0, groupimg)
    groupTransform1_2.connectInput(0, groupErodeSmooth1)

    param = groupErodeSmooth1.getParam("size")
    param.setExpression("thisGroup.defocussize.get()*-1", False, 0)
    param.setExpression("thisGroup.defocussize.get()*-1", False, 1)
    del param
    param = groupTransform1.getParam("scale")
    param.setExpression("thisGroup.aspect.get()", False, 0)
    del param
    param = groupTransform1.getParam("disableNode")
    param.setExpression("if thisGroup.aspect.get() == 1:\n\tret = 1\nelse:\n\tret = 0", True, 0)
    del param
    param = groupTransform1_2.getParam("scale")
    param.setExpression("1/thisGroup.aspect.get()", False, 0)
    del param
    param = groupTransform1_2.getParam("disableNode")
    param.setExpression("if thisGroup.aspect.get() == 1:\n\tret = 1\nelse:\n\tret = 0", True, 0)
    del param

    try:
        extModule = sys.modules["lp_fakeDefocusExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)