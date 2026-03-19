from app import create_app

app = create_app()

# This is required for IIS (wfastcgi looks for "app")
application = app

if __name__ == "__main__":
    app.run()