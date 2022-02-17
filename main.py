from selenium import webdriver
from time import sleep
import hashtagfile

# constants:
USERNAME = 'spectermindset'
PASSWORD = 'avocadomelon554ss'
DELAY = 3
PATH = 'C:\\chromedriver.exe'


class InstaBot:
    links = []

    def __init__(self):
        # handling path and running the page:
        hashtagfile.create_hashtag_file()
        hashtagfile.create_comment_file()

        self.comment_buffer = hashtagfile.get_comment()
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.instagram.com/')
        
        # timeout
        sleep(DELAY)

        self.enter()

        sleep(DELAY)

        self.navigate()

    def enter(self):

        # the web's login (username) input element:
        User_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name = USERNAME

        # the web's login (password) input element:
        if User_input != '':
            User_input.send_keys(user_name)

            pass_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            user_pass = PASSWORD
            pass_input.send_keys(user_pass)

        sleep(DELAY)

        submit_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        submit_btn.click()
        sleep(DELAY)
        dismiss_btn1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        dismiss_btn1.click()

    # not necessary if while sign in user don't have another notification
    # if user have, please uncomment those lines

    ''' 
        dismiss_btn2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        dismiss_btn2.click()
    '''

    def navigate(self):
        # import random hashtag from a file
        hashtag = hashtagfile.get_hastag()

        # get the html element of page's search bar
        search_bar_input = self.driver.find_element_by_xpath(
            "//input[@placeholder='Search']")

        # problems with selenium, if element wasn't found get it in another way
        if search_bar_input is None:
            search_bar_input = self.driver.find_element_by_class_name(
                'XTCLo d_djL DljaH')

        # send a random hashtag as an input to the SB
        search_bar_input.send_keys('#' + hashtag)

        sleep(DELAY)

        # html elem of selected hashtag feed page btn
        hash_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div['
            '1]/div/div')

        # click it
        hash_btn.click()
        sleep(5)

        # recognize post elements by their common tag ('a')
        links = self.driver.find_elements_by_tag_name("a")

        # return only the links of pages that are proper ('.com/p/ at the end')
        def link_visitor(post_link):
            return '.com/p/' in post_link.get_attribute(
                'href')

        # make a list of those links that are defined valid by our validation function
        valid_links = list(
            filter(link_visitor, links))

        for i in range(5):
            # post iteration
            link = valid_links[i].get_attribute('href')

            if link not in self.links:
                self.links.append(link)

        # interacting with the elements in the page (like, comment, post comment)
        for link in self.links:
            self.driver.get(link)
            sleep(DELAY)

            # perform likes:
            self.driver.find_element_by_class_name('fr66n').click()
            sleep(DELAY)

            # perform comments:
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(DELAY)
            commenter = self.driver.find_element_by_class_name('Ypffh')
            if commenter is None:
                commenter = self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
            commenter.send_keys(self.commentbuffer)
            sleep(DELAY)
            self.driver.find_element_by_xpath("//button[@type='submit']").click
            sleep(DELAY)


def main():
    InstaBot()


if __name__ == "__main__":
    main()
