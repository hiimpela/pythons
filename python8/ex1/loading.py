import importlib
import sys


def compare_managers() -> None:

    print("--- Dependency Managers Comparison ---")
    print("[pip] relies on requirements.txt (simple list file), requires "
          "manual venv creation")
    print("[Poetry] uses pyproject.toml, automatically makes a venv")


def check_dependencies() -> bool:

    required = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }
    missing = []

    print("LOADING STATUS: Loading programs...")
    print()

    for package, description in required.items():
        try:
            module = importlib.import_module(package)
            print(f"[OK] {package} ({module.__version__}) - {description}")

        except ImportError:
            print(f"[KO] missing {package}")
            missing.append(package)
    print()
    compare_managers()
    print()

    if missing:
        print(f"Error: missing dependencies: {', '.join(missing)}")
        print("Install with pip: pip install -r requirements.txt")
        print("Install with Poetry: poetry install && "
              "poetry run python loading.py")
        return False
    return True


def run_analysis() -> None:

    try:

        np = importlib.import_module("numpy")
        pd = importlib.import_module("pandas")
        plt = importlib.import_module("matplotlib.pyplot")

        print("Analyzing Matrix data...")
        num_points = 1000
        print(f"Processing {num_points} data points...")

        steps = np.arange(1, num_points + 1, dtype=np.float64)

        df = pd.DataFrame({"step": steps})

        phi = (1.0 + np.sqrt(5.0)) / 2.0
        golden_angle = 2.0 * np.pi / (phi ** 2)
        radii = df["step"] ** 0.53
        angles = df["step"] * golden_angle
        df["x"] = radii * np.cos(angles)
        df["y"] = radii * np.sin(angles)

        print("Generating visualization...")
        plt.figure(figsize=(7, 7), facecolor="#0a4f3a")
        plt.scatter(
            df["x"],
            df["y"],
            color="#0affd1",
            s=20,
            alpha=0.85,
        )
        plt.axis("equal")
        plt.axis("off")

        output_file = "matrix_analysis.png"
        plt.savefig(output_file, dpi=300)
        plt.close()

        print("Analysis complete!")
        print(f"Results saved to: {output_file}")

    except Exception as error:
        print(f"Error: Data stream corrupted during analysis: {error}")
        sys.exit(1)


def main() -> None:

    print()

    check_dependencies()
    run_analysis()


if __name__ == "__main__":
    main()
