import environ

project_root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, False),)

# read the .env file associated with the settings that're loaded
env.read_env('./application.env')