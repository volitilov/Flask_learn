# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Обработчики событий жизненного цикла

@before_first_request
# регестрирут функцию для вызова перед обработкой первого запроса

@before_request
# регестрирует функцию для вызова перед обработкой каждого запроса

@after_request
# регестрирует функцию для вызова после обработки каждого запроса, если не 
# возникло необработанных исключений

@teardown_request
# регестрирует функцию для вызова после обработки каждого запроса, если 
# возникло необработанное исключение


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

@errorhandler(code_or_exception)
# Декоратор, который используется для регистрации функции с учетом кода 
# ошибки.

