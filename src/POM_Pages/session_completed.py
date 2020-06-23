import json
from src.POM_Pages.session_data import SessionData
from src.POM_Pages.scroll_cards import ScrollCards


class SessionComplete:
    def __init__(self, driver):
        self.driver = driver
        self.card_details = SessionData(driver)
        self.scroll_card = ScrollCards(driver)

    def validate_and_return(self, data_item):
        self.driver.implicitly_wait(0)
        list_items = self.card_details.get_session_card_details()
        for key in data_item:
            for value in list_items:
                if value in data_item[key]:
                    data_item[key].remove(value)
        new_month = self.card_details.get_session_header_month()
        header_month = new_month[0]
        header_index = new_month[1]
        return list_items, header_month, header_index

    def scroll_to_end(self, stop_up_next=None):
        data = dict()
        count = 0
        list_box = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "rvScheduleList")]')
        previous_month = None
        previous_list = list()
        while True:
            returned_list = self.validate_and_return(data)
            update_list = returned_list[0]
            current_month = returned_list[1]
            current_month_index = returned_list[2]
            last_card = self.card_details.get_cards_list()[-1]

            if current_month is not None and current_month_index == 0:
                previous_month = current_month
                data[current_month] = update_list

            elif current_month is not None and current_month_index != 0:
                if previous_month is None:
                    previous_month = current_month
                if not data:
                    data[current_month] = list()
                for i in range(current_month_index):
                    if i < len(update_list):
                        data[previous_month].append(update_list[i])
                if (i+1) < len(update_list):
                    data[current_month] = update_list[i+1:]
                previous_month = current_month

            elif current_month is None:
                if previous_month is None:
                    data[current_month] = update_list
                else:
                    try:
                        data[previous_month] += update_list
                    except KeyError:
                        data[previous_month] = update_list
            if stop_up_next is True:
                for month in data:
                    for details in data[month]:
                        if details['Status'] == "UP NEXT":
                            with open(r'../../test_data/session_completed_data.json', 'w') as fp:
                                json.dump(data, fp, indent=4)
                            return data
            if previous_list == update_list:
                with open(r'../../test_data/session_data.json', 'w') as fp:
                    json.dump(data, fp, indent=4)
                return data
            else:
                previous_list.clear()
                previous_list += update_list

            self.scroll_card.scroll_by_card(last_card, list_box)
