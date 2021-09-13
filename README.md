# fabriq_test
## Запуск локально
- docker-compose up
- Добавление опроса и вопросов через django/admin
- Список активных опросов \
  GET localhost/quiz/active_quiz/
- Начать опрос \
  GET localhost/quiz/start/quiz/
      c параметрами {"quiz_id": "id"} \
  получаем список всех вопросов из опроса
- Ответ на впрос \
  POST localhost/quiz/start_quiz/
      c параметрами {"user": id, "quiz": id, "ask": id, ""text": data}
- Получение всех пройденных опросов юзера
  GET localhost/quiz/user_quiz/
      с параметрами {"user": id}
