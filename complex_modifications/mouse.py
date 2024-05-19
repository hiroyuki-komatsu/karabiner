import argparse
import pynput

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def parse_options() -> argparse.Namespace:
  """Parses given options in command line arguments.

  Returns:
    Parsed options.
  """
  parser = argparse.ArgumentParser()
  parser.add_argument('--position', help='XXX,YYY')
  parser.add_argument('--key', help='keyname of pynput')
  return parser.parse_args()


def mouse_position(x: int, y: int) -> None:
  mouse.position = (x, y)


def key_input(keyname : str) -> None:
  key = pynput.keyboard.HotKey.parse(f'<{keyname}>')
  keyboard.tap(key[0])


def main() -> None:
  options = parse_options()
  if options.position:
    x_str, y_str = options.position.split(',')
    mouse_position(int(x_str), int(y_str))
  if options.key:
    key_input(options.key)


if __name__ == '__main__':
  main()
