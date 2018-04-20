configs :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# документация на английском:
# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

default_config = ImmutableDict({
	'JSON_AS_ASCII': True, 
	'USE_X_SENDFILE': False, 
	'SESSION_COOKIE_PATH': None, 
	'SESSION_COOKIE_DOMAIN': None, 
	'SESSION_COOKIE_NAME': 'session', 
	'DEBUG': False, 
	'LOGGER_HANDLER_POLICY': 'always', 
	'LOGGER_NAME': None, 
	'SESSION_COOKIE_SECURE': False, 
	'SECRET_KEY': None, 
	'EXPLAIN_TEMPLATE_LOADING': False, 
	'MAX_CONTENT_LENGTH': None, 
	'PROPAGATE_EXCEPTIONS': None, 
	'APPLICATION_ROOT': None, 
	'SERVER_NAME': None, 
	'PREFERRED_URL_SCHEME': 'http', 
	'JSONIFY_PRETTYPRINT_REGULAR': True, 
	'TESTING': False, 
	'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 
	'TEMPLATES_AUTO_RELOAD': None, 
	'TRAP_BAD_REQUEST_ERRORS': False, 
	'JSON_SORT_KEYS': True, 
	'JSONIFY_MIMETYPE': 'application/json', 
	'SESSION_COOKIE_HTTPONLY': True, 
	'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 
	'PRESERVE_CONTEXT_ON_EXCEPTION': None, 
	'SESSION_REFRESH_EACH_REQUEST': True, 
	'TRAP_HTTP_EXCEPTIONS': False
})