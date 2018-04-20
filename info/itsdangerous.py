# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# itsdangerous

Signer
# Класс Signer может использоваться для присоединения подписи к 
# определенной строке:

> from itsdangerous import Signer
> s = Signer('secret-key')
> s.sign('my string') # 'my string.wh6tMHxLgJqB6oY1uT73iMlyrOA'
> s.unsign('my string.wh6tMHxLgJqB6oY1uT73iMlyrOA') # 'my string'



TimeStampSigner
# Если надо закончить подписку, можно использовать класс 
# TimestampSigner, который будет дополнительно помещать информацию 
# о отметке времени и подписывать ее. При несогласованности можно 
# подтвердить, что временная метка не истекает:

> from itsdangerous import TimestampSigner
> s = TimestampSigner('secret-key')
> string = s.sign('foo')
> s.unsign(string, max_age=5)
Traceback (most recent call last):
  ...
itsdangerous.SignatureExpired: Signature age 15 > 5 seconds



Serializer
# Поскольку строки трудно обрабатывать, этот модуль также 
# обеспечивает интерфейс сериализации, подобный json / pickle 
# и другим. (Внутри он использует simplejson по умолчанию, 
# однако это может быть изменено путем подклассификации.) Класс 
# Serializer реализует следующее:

> from itsdangerous import Serializer
> s = Serializer('secret-key')

> s.dumps([1, 2, 3, 4]) # '[1, 2, 3, 4].r7R9RhGgDPvvWl3iNzLuIIfELmo'
# метод dumps() генерирует цифровую подпись для данных, переданных
# в аргументе и затем сериализует данные с подписью в строковый
# маркер

> s.loads('[1, 2, 3, 4].r7R9RhGgDPvvWl3iNzLuIIfELmo') # [1, 2, 3, 4]
# метод loads() расшифровывает маркер. Функция проверяет сигнатуры
# и срок хранения и если всё в порядке, возвращает исходные данные.
# Когда метод loads() получает недопустимый маркер или определяет,
# что срок хранения истёк, он возбуждает исключение. 


URLSafeSerialize
> from itsdangerous import URLSafeSerializer
> s = URLSafeSerializer('secret-key')
> s.dumps([1, 2, 3, 4]) # 'WzEsMiwzLDRd.wSPHqC0gR7VUqivlSukJ0IeTDgo'
> s.loads('WzEsMiwzLDRd.wSPHqC0gR7VUqivlSukJ0IeTDgo') # [1, 2, 3, 4]

> s1 = URLSafeSerializer('secret-key', salt='activate-salt')
> s1.dumps(42) # 'NDI.kubVFOOugP5PAIfEqLJbXQbfTxs'
> s2 = URLSafeSerializer('secret-key', salt='upgrade-salt')
> s2.dumps(42) # 'NDI.7lx-N1P-z2veJ7nT1_2bnTkjGTE'
> s2.loads(s2.dumps(42)) # 42



JSONWebSignatureSerializer
# Они, как правило, очень похожи на уже существующий безопасный 
# сериализатор URL, но будут излучать заголовки в соответствии с 
# текущим проектом JSON Web Signature (JWS).

> from itsdangerous import JSONWebSignatureSerializer
> s = JSONWebSignatureSerializer('secret-key')
> s.dumps({'x': 42})
> 'eyJhbGciOiJIUzI1NiJ9.eyJ4Ijo0Mn0.ZdTn1YyGz9Yx5B5wNpWRL221G1WpVE5fPCPKNuc6UAo'



TimedJSONWebSignatureSerializer
# Генерирут веб-сигнатуры JSON с определённым сроком действия

> from itsdangerous import TimedJSONWebSignatureSerializer as S

> s = S('secret-key', expires_in=3600)
# аргумент epires_in определяет срок действия маркера в секундах 

> token = s.dumps({ 'confirm': 23 })
> data = s.loads(token)
> data # { 'confirm': 23 }
