from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("play_a_game.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Random Game Launcher",
    options = options,
    version = "0.1",
    description = 'Launches a random game',
    executables = executables
)