from typing import Union


def get_mask_card_number(card_number: Union[str, int, None]) -> str:
    """получает 20-ти значный номер карты и преобразовывает его полную маску"""
    if card_number == None:
        return "0"
    else:
        card_number = str(card_number)
        if len(card_number) > 20:
            return "слишком длинный номер карты"
        else:
            if not card_number.isdigit():
                return "присутствие нечисловых символов"

            else:
                card_number_merge = (
                    card_number[:6]
                    + "*" * (len(card_number) - len(card_number[:6]) - len(card_number[-4:]))
                    + card_number[-4:]
                )
                card_number_mask = ""
                for i in card_number_merge:
                    if (len(card_number_mask) - card_number_mask.count(" ")) % 4 == 0 and card_number_mask != "":
                        card_number_mask += " " + i
                    else:
                        card_number_mask += i
                return card_number_mask


def card_number_mask(card_number: Union[str, int]) -> str:
    """получает 20-ти значный номер карты и преобразовывает его короткую маску"""
    if card_number == None:
        return "0"
    else:
        card_number = str(card_number)
        if len(card_number) > 20:
            return "слишком длинный номер карты"
        else:
            if not card_number.isdigit():
                return "присутствие нечисловых символов"
            else:
                card_number_mask = "**" + card_number[-4:]
                return card_number_mask
