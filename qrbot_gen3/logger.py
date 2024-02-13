import logging
from logging.handlers import RotatingFileHandler
import os

# Путь к директории логов
log_directory = "logs"
# Имя файла лога
log_file_name = "bot.log"
# Полный путь к файлу лога
log_file_path = os.path.join(log_directory, log_file_name)

# Создание директории для логов, если она не существует
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка базовой конфигурации логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логов, которые будут записываться
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Формат логов
)

# Добавление RotatingFileHandler для ротации логов
handler = RotatingFileHandler(log_file_path, maxBytes=10000000, backupCount=5)
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

# Получение экземпляра логгера и добавление обработчика
logger = logging.getLogger(__name__)
logger.addHandler(handler)

# Для добавления обработчика вывода логов в консоль (опционально)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)
