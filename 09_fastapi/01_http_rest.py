"""HTTP и REST — на чём стоит FastAPI. Коды статусов учи наизусть."""

# клиент (браузер, приложение) → запрос → сервер → ответ (статус + тело JSON)

# метод     смысл              идемпотентен? (повтор безопасен)
# GET       получить           да
# POST      создать            нет
# PUT       заменить целиком   да
# PATCH     изменить поля      обычно да
# DELETE    удалить            да

# URL:  https://api.site.ru/api/v1/tasks/5?done=false
#        схема   хост          путь              query

# статусы
# 200 OK                 успех, есть тело
# 201 Created            создали
# 204 No Content         успех, тела нет (часто DELETE)
# 400 Bad Request        кривой запрос
# 401 Unauthorized       не вошёл (нет/протух токен)
# 403 Forbidden          вошёл, но нельзя
# 404 Not Found          нет ресурса
# 409 Conflict           дубль (email занят)
# 422 Unprocessable      валидация Pydantic
# 429 Too Many Requests  лимит
# 500 / 503              ошибка / сервер недоступен

# REST-договорённости:
# GET    /tasks          список
# GET    /tasks/5        один
# POST   /tasks          создать  тело JSON
# PATCH  /tasks/5        частично
# DELETE /tasks/5        удалить
# фильтры: /tasks?done=false&limit=20&page=2
# ошибки одного вида: {"detail": "..."}  (так по умолчанию FastAPI)

# заголовки: Content-Type: application/json
#            Authorization: Bearer <jwt>
# timeout на клиенте ВСЕГДА; токен в .env
