from app import create_app

app = create_app('default')  # Use the appropriate configuration

if __name__ == "__main__":
    app.run()