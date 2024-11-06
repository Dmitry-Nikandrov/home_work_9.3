import logging
from logging import getLogger
from typing import Union

get_mask_card_logger = logging.getLogger("get_mask_card")
get_mask_card_handler = logging.FileHandler(filename="../logs/get_mask_card.log", mode="w", encoding="utf-8")
get_mask_card_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s - %(funcName)s - %(name)s - %(levelname)s - %(message)s"
)
get_mask_card_handler.setFormatter(get_mask_card_formatter)
get_mask_card_logger.addHandler(get_mask_card_handler)
get_mask_card_logger.setLevel(logging.DEBUG)

get_mask_account_logger = getLogger("get_mask_account")
get_mask_account_handler = logging.FileHandler(filename="../logs/get_mask_account.log", mode="w", encoding="utf-8")
get_mask_account_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s - %(funcName)s - %(name)s - %(levelname)s - %(message)s"
)
get_mask_account_handler.setFormatter(get_mask_account_formatter)
get_mask_account_logger.addHandler(get_mask_account_handler)
get_mask_account_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str, int, None]) -> str:
    """получает 20-ти значный номер карты и преобразовывает его полную маску"""
    if card_number is None:
        get_mask_card_logger.warning("Номер карты не задан")
        return "0"
    else:
        card_number = str(card_number)
        if len(card_number) > 20:
            get_mask_card_logger.warning("слишком длинный номер карты")
            return "слишком длинный номер карты"
        else:
            if not card_number.isdigit():
                get_mask_card_logger.warning("присутствие нечисловых символов")
                return "присутствие нечисловых символов"

            else:
                str_long = len(card_number) - len(card_number[:6]) - len(card_number[-4:])
                card_number_merge = card_number[:6] + "*" * str_long + card_number[-4:]
                card_number_mask = ""
                for i in card_number_merge:
                    if (len(card_number_mask) - card_number_mask.count(" ")) % 4 == 0 and card_number_mask != "":
                        card_number_mask += " " + i
                    else:
                        card_number_mask += i
                get_mask_card_logger.info(f"маска номера карты: {card_number_mask}")
                return card_number_mask


"Примеры логирования функции get_mask_card_number с записью в соответствующем файле .log в папке logs"
print(get_mask_card_number(1234567890123456789011))
print(get_mask_card_number(123456789012345678901111))
print(get_mask_card_number("1234567890123456701a"))
print(get_mask_card_number(12345678901234567890))


def get_mask_account(card_number: Union[str, int, None]) -> str:
    """получает 20-ти значный номер карты и преобразовывает его короткую маску"""
    if card_number is None:
        get_mask_account_logger.warning("Номер карты не задан")
        return "0"
    else:
        card_number = str(card_number)
        if len(card_number) > 20:
            get_mask_account_logger.warning("число цифр в счете больше 20")
            return "число цифр в счете больше 20"
        else:
            if not card_number.isdigit():
                get_mask_account_logger.warning("присутствие нечисловых символов")
                return "присутствие нечисловых символов"
            else:
                card_number_mask = "**" + card_number[-4:]
                get_mask_account_logger.warning(f"маска номера карты: {card_number_mask}")
                return card_number_mask


"Примеры логирования функции get_mask_account с записью в соответствующем файле .log в папке logs"
print(get_mask_account(None))
print(get_mask_account(98765432109876543219911))
print(get_mask_account("9876543210987654321ф"))
print(get_mask_account(98765432109876543211))
