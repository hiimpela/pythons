import sys
import os
import site


def main() -> None:

    in_venv = sys.prefix != sys.base_prefix
    py_path = sys.executable if in_venv else os.path.realpath(sys.executable)
    venv_name = os.path.basename(py_path) if in_venv else "None Detected"

    print()
    if in_venv:
        print("MATRIX STATUS: Welcome to the construct")
    else:
        print("MATRIX STATUS: You're still plugged in")
    print()

    print(f"Current Python: {py_path}")
    print(f"Virtual Environment: {venv_name}")

    if not in_venv:
        print()
        print("WARNING: You're in the global environment!",
              "The machines can see everything you install.",
              '',
              "To enter the construct, run:",
              "python3 -m venv matrix_env",
              "source matrix_env/bin/activate # On Unix",
              "matrix_env\\Scripts\\activate # On Windows",
              '',
              "Then run this program again.", sep='\n')
        return

    print(f"Environment path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!",
          "Safe to install packages without affecting",
          "the global system.", sep='\n')

    print()
    print("Package installation path:")
    print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()
