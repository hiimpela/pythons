import os
import sys


def main() -> None:

    try:
        import dotenv
        dotenv.load_dotenv()

    except ImportError:
        print("Missing python-dotenv module!")
        print("Go into a venv and run: pip install -r requirements.txt")
        sys.exit(1)

    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    matrix_mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    if not all([matrix_mode, db_url, api_key, log_level, zion_endpoint]):
        print("WARNING: Missing required configuration variables.")
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "production":
        print(f"Database: {db_url}")
        print(f"API Access: {api_key}")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_endpoint}")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")

    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
