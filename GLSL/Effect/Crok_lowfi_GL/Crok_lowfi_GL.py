# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_lowfi_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_lowfi_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_lowfi_GL"

def getLabel():
    return "Crok_lowfi_GL"

def getVersion():
    return 1.1

def getIconPath():
    return "Crok_lowfi_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "Simulates NES, EGA and Gameboy video out."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(1, 0.2353, 0.2353)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat0", "Brightness : ")
    param.setMinimum(0, 0)
    param.setMaximum(10, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createChoiceParam("graphicMode", "Graphic mode : ")
    entries = [ ("NES", ""),
    ("GAMEBOY", ""),
    ("EGA", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.graphicMode = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createSeparatorParam("OPTIONS", "Options")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OPTIONS = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createBooleanParam("isPremult", "Source is premultiplied : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Source is premultiplied.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(True)
    lastNode.isPremult = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Crok_lowfi_GL v1.1")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE101", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE101 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2019)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4392)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3301)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4139, 3866)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueInt1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/run/media/ffernandez/FABRICE/PERSO/NATRON/GIT_DEV/natron-plugins/Shadertoy/crok_lowfi.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("\n//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : crok_lowfi Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : crok_lowfi Matchbox for Autodesk Flame\n\n\n// iChannel0: Source, filter=nearest, wrap=clamp\n// BBox: iChannel0\n\n// https://www.shadertoy.com/view/MdfXDH#\n\nuniform float brightness = 1.0; // Brightness : (brightness), min =0.0, max=10.0\n\nuniform int graphicMode = 0; // Graphic mode : (graphic mode), min=0, max=2\n\nuniform bool NES = true; // NES : (NES)\nuniform bool GAMEBOY = false; // GAMEBOY : (GAMEBOY)\nuniform bool EGA = false; // EGA : (EGA)\n\n\n\nvec3 find_closest_nes (vec3 ref) {\t\n\tvec3 old_nes = vec3 (100.0 *255.0);\t\t\n\t#define TRY_COLOR(new) old_nes = mix (new, old_nes, step (length (old_nes-ref), length (new-ref)));\t\n\tTRY_COLOR (vec3 (0.0, 88.0, 0.0));\n\tTRY_COLOR (vec3 (80.0, 48.0, 0.0));\n\tTRY_COLOR (vec3 (0.0, 104.0, 0.0));\n\tTRY_COLOR (vec3 (0.0, 64.0, 88.0));\n\tTRY_COLOR (vec3 (0.0, 120.0, 0.0));\n\tTRY_COLOR (vec3 (136.0, 020.0, 0.0));\n\tTRY_COLOR (vec3 (0.0, 168.0, 0.0));\n\tTRY_COLOR (vec3 (168.0, 16.0, 0.0));\n\tTRY_COLOR (vec3 (168.0, 0.0, 32.0));\n\tTRY_COLOR (vec3 (0.0, 168.0, 68.0));\n\tTRY_COLOR (vec3 (0.0, 184.0, 0.0));\n\tTRY_COLOR (vec3 (0.0, 0.0, 188.0));\n\tTRY_COLOR (vec3 (0.0, 136.0, 136.0));\n\tTRY_COLOR (vec3 (148.0, 0.0, 132.0));\n\tTRY_COLOR (vec3 (68.0, 40.0, 188.0));\n\tTRY_COLOR (vec3 (120.0, 120.0, 120.0));\n\tTRY_COLOR (vec3 (172.0, 124.0, 0.0));\n\tTRY_COLOR (vec3 (124.0, 124.0, 124.0));\n\tTRY_COLOR (vec3 (228.0, 0.0, 88.0));\n\tTRY_COLOR (vec3 (228.0, 92.0, 16.0));\n\tTRY_COLOR (vec3 (88.0, 216.0, 84.0));\n\tTRY_COLOR (vec3 (0.0, 0.0, 252.0));\n\tTRY_COLOR (vec3 (248.0, 56.0, 0.0));\n\tTRY_COLOR (vec3 (0.0, 88.0, 248.0));\n\tTRY_COLOR (vec3 (0.0, 120.0, 248.0));\n\tTRY_COLOR (vec3 (104.0, 68.0, 252.0));\n\tTRY_COLOR (vec3 (248.0, 120.0, 88.0));\n\tTRY_COLOR (vec3 (216.0, 0.0, 204.0));\n\tTRY_COLOR (vec3 (88.0, 248.0, 152.0));\n\tTRY_COLOR (vec3 (248.0, 88.0, 152.0));\n\tTRY_COLOR (vec3 (104.0, 136.0, 252.0));\n\tTRY_COLOR (vec3 (252.0, 160.0, 68.0));\n\tTRY_COLOR (vec3 (248.0, 184.0, 0.0));\n\tTRY_COLOR (vec3 (184.0, 248.0, 24.0));\n\tTRY_COLOR (vec3 (152.0, 120.0, 248.0));\n\tTRY_COLOR (vec3 (0.0, 232.0, 216.0));\n\tTRY_COLOR (vec3 (60.0, 188.0, 252.0));\n\tTRY_COLOR (vec3 (188.0, 188.0, 188.0));\n\tTRY_COLOR (vec3 (216.0, 248.0, 120.0));\n\tTRY_COLOR (vec3 (248.0, 216.0, 120.0));\n\tTRY_COLOR (vec3 (248.0, 164.0, 192.0));\n\tTRY_COLOR (vec3 (0.0, 252.0, 252.0));\n\tTRY_COLOR (vec3 (184.0, 184.0, 248.0));\n\tTRY_COLOR (vec3 (184.0, 248.0, 184.0));\n\tTRY_COLOR (vec3 (240.0, 208.0, 176.0));\n\tTRY_COLOR (vec3 (248.0, 120.0, 248.0));\n\tTRY_COLOR (vec3 (252.0, 224.0, 168.0));\n\tTRY_COLOR (vec3 (184.0, 248.0, 216.0));\n\tTRY_COLOR (vec3 (216.0, 184.0, 248.0));\n\tTRY_COLOR (vec3 (164.0, 228.0, 252.0));\n\tTRY_COLOR (vec3 (248.0, 184.0, 248.0));\n\tTRY_COLOR (vec3 (248.0, 216.0, 248.0));\n\tTRY_COLOR (vec3 (248.0, 248.0, 248.0));\n\tTRY_COLOR (vec3 (252.0, 252.0, 252.0));\t\n\n\treturn old_nes ;\n}\n\nvec3 find_closest_gb (vec3 ref_gb) {\t\n\tvec3 old_gb = vec3 (100.0 *255.0);\t\t\n\t#define TRY_COLOR_gb(new) old_gb = mix (new, old_gb, step (length (old_gb-ref_gb), length (new-ref_gb)));\t\n\tTRY_COLOR_gb (vec3 (156.0, 189.0, 15.0));\n\tTRY_COLOR_gb (vec3 (140.0, 173.0, 15.0));\n\tTRY_COLOR_gb (vec3 (48.0, 98.0, 48.0));\n\tTRY_COLOR_gb (vec3 (15.0, 56.0, 15.0));\n\t\n\treturn old_gb ;\n}\n\nvec3 find_closest_ega (vec3 ref_ega) {\t\n\tvec3 old_ega = vec3 (100.0 *255.0);\t\t\n\t#define TRY_COLOR_ega(new) old_ega = mix (new, old_ega, step (length (old_ega-ref_ega), length (new-ref_ega)));\t\n    TRY_COLOR_ega (vec3 (0.0, 0.0, 0.0)); \n    TRY_COLOR_ega (vec3 (255.0,255.0,255.0)); \n    TRY_COLOR_ega (vec3 (255.0,  0.0,  0.0)); \n    TRY_COLOR_ega (vec3 (  0.0,255.0,  0.0)); \n    TRY_COLOR_ega (vec3 (  0.0,  0.0,255.0)); \n    TRY_COLOR_ega (vec3 (255.0,255.0,  0.0)); \n    TRY_COLOR_ega (vec3 (  0.0,255.0,255.0)); \n    TRY_COLOR_ega (vec3 (255.0,  0.0,255.0)); \n    TRY_COLOR_ega (vec3 (128.0,  0.0,  0.0)); \n    TRY_COLOR_ega (vec3 (  0.0,128.0,  0.0)); \n    TRY_COLOR_ega (vec3 (  0.0,  0.0,128.0)); \n    TRY_COLOR_ega (vec3 (128.0,128.0,  0.0)); \n    TRY_COLOR_ega (vec3 (  0.0,128.0,128.0)); \n    TRY_COLOR_ega (vec3 (128.0,  0.0,128.0)); \n    TRY_COLOR_ega (vec3 (128.0,128.0,128.0)); \n    TRY_COLOR_ega (vec3 (255.0,128.0,128.0)); \n\n\treturn old_ega ;\n}\n\n\nfloat dither_matrix (float x, float y) {\n\treturn mix(mix(mix(mix(mix(mix(0.0,32.0,step(1.0,y)),mix(8.0,40.0,step(3.0,y)),step(2.0,y)),mix(mix(2.0,34.0,step(5.0,y)),mix(10.0,42.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),mix(mix(mix(48.0,16.0,step(1.0,y)),mix(56.0,24.0,step(3.0,y)),step(2.0,y)),mix(mix(50.0,18.0,step(5.0,y)),mix(58.0,26.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),step(1.0,x)),mix(mix(mix(mix(12.0,44.0,step(1.0,y)),mix(4.0,36.0,step(3.0,y)),step(2.0,y)),mix(mix(14.0,46.0,step(5.0,y)),mix(6.0,38.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),mix(mix(mix(60.0,28.0,step(1.0,y)),mix(52.0,20.0,step(3.0,y)),step(2.0,y)),mix(mix(62.0,30.0,step(5.0,y)),mix(54.0,22.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),step(3.0,x)),step(2.0,x)),mix(mix(mix(mix(mix(3.0,35.0,step(1.0,y)),mix(11.0,43.0,step(3.0,y)),step(2.0,y)),mix(mix(1.0,33.0,step(5.0,y)),mix(9.0,41.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),mix(mix(mix(51.0,19.0,step(1.0,y)),mix(59.0,27.0,step(3.0,y)),step(2.0,y)),mix(mix(49.0,17.0,step(5.0,y)),mix(57.0,25.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),step(5.0,x)),mix(mix(mix(mix(15.0,47.0,step(1.0,y)),mix(7.0,39.0,step(3.0,y)),step(2.0,y)),mix(mix(13.0,45.0,step(5.0,y)),mix(5.0,37.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),mix(mix(mix(63.0,31.0,step(1.0,y)),mix(55.0,23.0,step(3.0,y)),step(2.0,y)),mix(mix(61.0,29.0,step(5.0,y)),mix(53.0,21.0,step(7.0,y)),step(6.0,y)),step(4.0,y)),step(7.0,x)),step(6.0,x)),step(4.0,x));\n}\n\nvec3 dither (vec3 color, vec2 uv) {\t\n\n\t\n\tif ( graphicMode==0 )\n\t{\n\t\tcolor *= 255.0 * 0.8* brightness;\t\n\t\tcolor += dither_matrix (mod (uv.x, 8.0), mod (uv.y, 8.0 )) ;\n\t\tcolor = find_closest_nes (clamp (color, 0.0, 255.0));\n\t\treturn color / 255.0;\n}\n\n\tif ( graphicMode==1 )\n\t{\n\t\tcolor *= 255.0 * 0.55* brightness;\n\t\tcolor += dither_matrix (mod (uv.x, 8.0), mod (uv.y, 8.0 )) ;\n\t\tcolor = find_closest_gb (clamp (color, 0.0, 255.0));\n\t\treturn color / 255.0;\n\t}\n\n\tif ( graphicMode==2 )\n\t{\n\t\tcolor *= 255.0 * 0.9* brightness;\n\t\tcolor += dither_matrix (mod (uv.x, 8.0), mod (uv.y, 8.0 )) ;\n\t\tcolor = find_closest_ega (clamp (color, 0.0, 255.0));\n\t\treturn color / 255.0;\n\t}\n\t\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 uv = fragCoord.xy / iResolution.xy;\n\tvec3 tc = texture2D(iChannel0, uv).xyz;\n\tfragColor =  vec4 (dither (tc, fragCoord.xy),1.0);\t\n}")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("brightness")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Brightness :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("brightness")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("graphicMode")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Graphic mode :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("graphic mode")
        del param

    param = lastNode.getParam("paramMinInt1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt1")
    if param is not None:
        param.setValue(2, 0)
        del param

    del lastNode
    # End of node "Shadertoy1"

    # Start of node "Unpremult1"
    lastNode = app.createNode("net.sf.openfx.Unpremult", 2, group)
    lastNode.setScriptName("Unpremult1")
    lastNode.setLabel("Unpremult1")
    lastNode.setPosition(4138, 3712)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupUnpremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Unpremult1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(4171, 3607)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(4319, 3607)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Premult1"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult1")
    lastNode.setLabel("Premult1")
    lastNode.setPosition(4140, 4148)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupPremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Premult1"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(4140, 4021)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(4317, 4031)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupPremult1)
    groupShadertoy1.connectInput(0, groupUnpremult1)
    groupUnpremult1.connectInput(0, groupDot1)
    groupDot1.connectInput(0, groupSource)
    groupDot2.connectInput(0, groupDot1)
    groupPremult1.connectInput(0, groupShuffle1)
    groupShuffle1.connectInput(0, groupShadertoy1)
    groupShuffle1.connectInput(1, groupDot3)
    groupDot3.connectInput(0, groupDot2)

    param = groupShadertoy1.getParam("paramValueFloat0")
    group.getParam("Shadertoy1paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueInt1")
    param.setExpression("thisGroup.graphicMode.get()", False, 0)
    del param
    param = groupUnpremult1.getParam("disableNode")
    param.setExpression("not thisGroup.isPremult.get()", False, 0)
    del param
    param = groupPremult1.getParam("disableNode")
    param.setExpression("not thisGroup.isPremult.get()", False, 0)
    del param

    try:
        extModule = sys.modules["Crok_lowfi_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
