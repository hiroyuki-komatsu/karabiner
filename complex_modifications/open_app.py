import argparse
import subprocess

APPS = {
  'f1': 'open /System/Applications/Dictionary.app',
  'f2': 'open ~/Applications/Chrome\ Apps.localized/SecureShell.app',
  'f3': 'open ~/Applications/Chrome\ Apps.localized/Cider-v.app',
  'f4': 'open ~/Applications/Chrome\ Apps.localized/2023\ Notes.app',
  'f6': 'open  /Applications/Karabiner-Elements.app',
  'f11': 'open /System/Library/PreferencePanes/Displays.prefPane/',
  'f12': 'open /System/Applications/Utilities/Terminal.app',
  'f13': 'open /Applications/Visual\ Studio\ Code.app',
  'f16': 'open /Applications/Karabiner-EventViewer.app',
}


def parse_options() -> argparse.Namespace:
  """Parses given options in command line arguments.

  Returns:
    Parsed options.
  """
  parser = argparse.ArgumentParser()
  parser.add_argument('--key', help='key for the app.')
  return parser.parse_args()


def main() -> None:
  options = parse_options()
  command = APPS.get(options.key)
  if command:
    subprocess.run(command, shell=True)


if __name__ == '__main__':
  main()
