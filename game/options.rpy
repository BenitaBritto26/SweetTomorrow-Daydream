## Basics ######################################################################

define config.name = _("Sweet Tomorrow")
define config.version = "1.0"
define build.name = "Sweet Tomorrow"

## Main menu ##################################################################
# Main menu background is now set via gui.rpy / screen main_menu
define gui.show_name = False

## About screen info ##########################################################
define gui.about = _("An innocent schoolgirl named Amelia relies on your help to make her decisions: getting ready for school, packing her lunch, and much more. But your choices will define her fate, and whether her deepest, darkest secrets are revealed.")

## Sound and Music ############################################################
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Transitions ################################################################
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

## Preferences ################################################################
default preferences.text_cps = 0
default preferences.afm_time = 15

## Save directory #############################################################
define config.save_directory = "Daydream-1758990533"

## Window icon ################################################################
define config.window_icon = "gui/window_icon.png"

## Build configuration ########################################################
init python:
    # Exclude unnecessary files from build
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    # Archive images if desired
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    # Include documentation in builds
    build.documentation('*.html')
    build.documentation('*.txt')
