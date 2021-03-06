# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named TimeLoopExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from TimeLoopExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.TimeLoop"

def getLabel():
    return "TimeLoop"

def getVersion():
    return 1

def getIconPath():
    return "TimeLoop.png"

def getGrouping():
    return "Community/Time"

def getPluginDescription():
    return "This Pyplug create loops from the input clip, set the start value for the first frame of the loop, then the loop duration (length)"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createIntParam("start", "start")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("the starting frame of the loop")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.start = param
    del param

    param = lastNode.createIntParam("length", "length")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("the length of the loop in frames")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(20, 0)
    lastNode.length = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Node'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "TimeOffset1"
    lastNode = app.createNode("net.sf.openfx.timeOffset", 1, group)
    lastNode.setScriptName("TimeOffset1")
    lastNode.setLabel("TimeOffset1")
    lastNode.setPosition(811, 219)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.65, 0.35)
    groupTimeOffset1 = lastNode

    param = lastNode.getParam("timeOffset")
    if param is not None:
        param.setValue(148, 0)
        del param

    del lastNode
    # End of node "TimeOffset1"

    # Start of node "input"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("input")
    lastNode.setLabel("input")
    lastNode.setPosition(808, 84)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupinput = lastNode

    del lastNode
    # End of node "input"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(811, 426)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupTimeOffset1.connectInput(0, groupinput)
    groupOutput1.connectInput(0, groupTimeOffset1)

    param = groupTimeOffset1.getParam("timeOffset")
    param.setExpression("(range(0,frame,(thisGroup.length.get()+1)).pop(-1))-(thisGroup.start.get()-1)", False, 0)
    del param

    try:
        extModule = sys.modules["TimeLoopExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
