

# ========== ДЕТАЛЬНАЯ ИНСТРУКЦИЯ ПО РАБОЧЕМУ ПРОЦЕССУ GIT ==========
# В этом файле описан рабочий процесс Git от локального репозитория до удаленного,
#! включая команды init, add, commit, (add origin) push и pull.

# =================== 1. ИНИЦИАЛИЗАЦИЯ И УСТАНОВКА REPO ===================
# **Создание нового локального репозитория**
# Перейдите в папку вашего проекта и инициализируйте репозиторий:
#! git init
# Это создаст скрытую папку .git, которая будет отслеживать изменения.

# =================== 2. ДОБАВЛЕНИЕ ФАЙЛОВ В СТАДИЮ (STAGING AREA) ===================
# **Добавление изменений для отслеживания**
# После того как вы внесли изменения в файлы, используйте команду:
#! git add <имя_файла>
# Например, чтобы добавить файл script.py:
#! git add script.py
# Чтобы добавить все изменения в текущем каталоге:
#! git add .
# Это помещает изменения в "стадию" (staging area), готовя их к коммиту.

# =================== 3. СОЗДАНИЕ КОММИТА ===================
# **Фиксация изменений с сообщением**
# После добавления файлов в стадию, вы можете зафиксировать изменения с помощью команды:
#! git commit -m "Сообщение коммита"
# Например:
# git commit -m "Добавил новый функционал в script.py"
# Это создаёт снимок вашего проекта на данный момент времени и сохраняет изменения в локальном репозитории.

#* =================== 4. ПУШ ИЗМЕНЕНИЙ В УДАЛЕННЫЙ РЕПОЗИТОРИЙ ===================
# **Отправка локальных изменений на GitHub**
#! Инициализировать (добавить) удаленный репо
# После создания коммита вы можете отправить изменения в удалённый репозиторий (например, на GitHub):
#! git push origin <имя_ветки>
# Например, чтобы отправить изменения в ветку main:
# git push origin main
# Эта команда обновляет удалённый репозиторий, передавая все изменения из вашей локальной ветки.

# =================== 5. ПОЛУЧЕНИЕ ИЗМЕНЕНИЙ ИЗ УДАЛЕННОГО РЕПОЗИТОРИЯ ===================
# **Синхронизация локального репозитория с удалённым**
# Чтобы получить изменения из удалённого репозитория, используйте команду:
#! git pull origin <имя_ветки>
# Например, чтобы получить изменения из ветки main:
# git pull origin main
# Эта команда загружает последние изменения из удалённого репозитория и объединяет их с вашей локальной веткой.

# =================== 6. ЗАВЕРШЕНИЕ ===================
# В результате последовательного выполнения этих команд вы сможете:
# 1. Добавлять изменения в локальный репозиторий.
# 2. Фиксировать эти изменения.
# 3. Отправлять их на удалённый репозиторий.
# 4. Синхронизировать локальный репозиторий с удалённым, получая последние изменения.

# Эти команды являются основой рабочего процесса Git и помогут вам эффективно управлять версиями вашего кода.
