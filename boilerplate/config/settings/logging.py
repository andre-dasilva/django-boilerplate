LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'when': 'D',
            'backupCount': 0,
            'filename': './logs/boilerplate.log'
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
    },
    # To log every db activity use django.db.backends logger, to log everything use django
    # 'loggers': {
    #     'django.db.backends': {
    #         'handlers': ['console'],
    #         'level': 'DEBUG',
    #         'propagate': False,
    #     },
    # },
}