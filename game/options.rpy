## Basics ######################################################################

define config.name = _("Daydream")
define config.version = "1.0"
define build.name = "Daydream"

## Main menu ##################################################################

define config.main_menu_background = "gui/startscreen.png"
define gui.show_name = True

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

    # To archive images, uncomment:
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    # Include documentation
    build.documentation('*.html')
    build.documentation('*.txt')
