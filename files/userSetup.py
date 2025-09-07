from maya import cmds, utils

cmds.optionVar(intValue=('showHomeScreenOnStartup', 0))
cmds.optionVar(intValue=('showHomeMenubarIcon', 0))
cmds.whatsNewHighlight(showStartupDialog=False, highlightOn=False)


def setup_viewport() -> None:
	cmds.setAttr("hardwareRenderingGlobals.renderMode", 4)
	cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 1)
	cmds.setAttr("hardwareRenderingGlobals.lineAAEnable", 1)
	cmds.setAttr("hardwareRenderingGlobals.multiSampleCount", 8)
	cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 1)
	print("Viewport defaults applied successfully.")


def configure_grid() -> None:
	cmds.grid(displayAxes=True, displayAxesBold=True, displayDivisionLines=True, displayGridLines=True, displayOrthographicLabels=True, displayPerspectiveLabels=True, divisions=10, size=50, spacing=5, orthographicLabelPosition="edge", perspectiveLabelPosition="axis")
	cmds.displayColor('grid', 2)  # Subdivision lines
	cmds.displayColor('gridAxis', 23)  # Axes
	cmds.displayColor('gridHighlight', 3)  # Grid lines & numbers
	print("Grid defaults applied successfully.")


def configure_colors() -> None:
	cmds.displayPref(displayGradient=True)
	cmds.displayRGBColor('backgroundTop', 0.20, 0.01, 0.25)
	cmds.displayRGBColor('backgroundBottom', 0.04, 0.18, 0.23)
	print("Color defaults applied successfully.")


def configure_panels() -> None:
	cmds.workspaceControl("ToolBox", edit=True, visible=False)
	cmds.workspaceControl("HelpLine", edit=True, visible=False)
	print("Panel defaults applied successfully.")


def run_after_ui_init() -> None:
	utils.executeDeferred(setup_viewport)
	utils.executeDeferred(configure_grid)
	utils.executeDeferred(configure_panels)
	utils.executeDeferred(configure_colors)


utils.executeDeferred(run_after_ui_init)
