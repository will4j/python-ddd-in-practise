from infrastructure.adapters.rest import app

if __name__ == '__main__':
    bind = "127.0.0.1:8000"

    app.run(bind=bind)
