import aiohttp
import xml.etree.ElementTree as ET
from config import CURRENCY_API_URL


async def get_dollar_rate():
    async with aiohttp.ClientSession() as session:
        async with session.get(CURRENCY_API_URL) as response:
            # Проверяем статус ответа
            if response.status == 200:
                # Получаем XML данные
                xml_data = await response.text()
                # Парсим XML
                root = ET.fromstring(xml_data)
                # Ищем курс доллара
                for item in root.findall(".//Valute"):
                    if item.find("CharCode").text == "USD":
                        return float(
                            item.find("Value").text.replace(",", ".")
                        )  # Преобразуем строку в float
            else:
                return "Не удалось получить данные о курсе"
