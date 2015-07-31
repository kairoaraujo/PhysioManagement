from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Physio Management'
settings.subtitle = 'Web system to Physiotherapist'
settings.author = 'Kairo Araujo'
settings.author_email = 'kairo@kairo.eti.br'
settings.keywords = 'physiotherapist, management, system, '
settings.description = 'Web system for Physiotherapists (and clinics) manager patients.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'f1d1d6e6-f529-4ef7-9941-b1013fbe03cd'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
