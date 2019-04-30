from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessageListPage(BaseAction):

    new_message_butten = By.ID,"com.android.mms:id/action_compose_new"

    def click_new_message(self):
        self.click(self.new_message_butten)