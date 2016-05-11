class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_BINDS = {
        'users': 'sqlite:///users.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = 'sf3tefjSFdajJt72DSF2dgzzx'
    UPLOAD_FOLDER = '/runtime'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
