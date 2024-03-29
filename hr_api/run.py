from hr_api.api.app import create_app
from hr_api.api.config import DevelopmentConfig

application = create_app(config_object=DevelopmentConfig)

if __name__ == '__main__':
    application.run()