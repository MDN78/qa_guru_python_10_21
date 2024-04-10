## Мобильная автоматизация #1. Browserstack
- Зарегистрировать аккаунт в https://browserstack.com  
- Запустить автотест из занятия локально  
- Разработать еще один автотест на открытие любой статьи (статья не будет отображена на browserstack(отображена будет ошибка), вам нужно реализовать только клик на то что вы ищите). Если хотите чтобы статью было видно, нужно залить свою апк википедии и работать с ней
- * Разработать еще один автотест на iOS  
- * Адаптировать conftest.py для работы с двумя типами платформ - Android, iOS
- * Вынести данные (логин, пароль, урл браузерстека и т.д.) в .env с pydantic
- Сделать сборку в дженкинсе

## Для запуска теста:
Preconditions: Необходимо предсоздание файлов `.env.local_emulator`, `.env.bstck`, `.env.local_real` и наполнить учетными данными  
1. Запуск на эмуляторе командой `pytest --context=local_emulator `  
2. Запуск на Browserstack:
   - Залить APK файл на платформу [согласно инструкции](https://github.com/qa-guru/mobile-tests-13-py/tree/demo-selene-appium-with-browserstack-android#how-to-upload-your-own-version-of-application-to-browserstack)
   - запуск командой терминала `pytest --context=bstack`
3. Запуск на реальном устройстве командой `pytest --context=local_real`  
4. Загрузка отчета Allure командой `allure serve`

