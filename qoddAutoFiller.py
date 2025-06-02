from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
driver = webdriver.Chrome()

with open("questionsAndAnswers.txt", "r") as my_file:
    questionAndAnswer = ""
    question = ""
    answer = ""
    response = requests.get('https://the-trivia-api.com/api/questions?categories=food_and_drink,general_knowledge,music,science,sport_and_leisure&limit=50&difficulty=easy')
    if response.status_code == requests.codes.ok:
        info = response.json()
        for dict in info:
            question = dict["question"]
            answer = dict["correctAnswer"]
            questionAndAnswer = question + " " + answer
            if questionAndAnswer in my_file:
                continue
            else:
                with open("questionsAndAnswers.txt", "a") as my_file2:
                    my_file2.write(questionAndAnswer + "\n")
            # Navigate to url
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLScW8oL31TV7JNV2f1XDst4R4iMfGUWNba3tdfBZsA-bhYDHaA/viewform")
            time.sleep(10)
            name = "Yao Amegandjin"
            firstLastNameBox = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

            # Enter First and Last name
            firstLastNameBox.send_keys(name)

            # Clear QODD Question field to empty it from any previous data
            qoddQuestion = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

            # Enter question
            qoddQuestion.send_keys(question)

            # Clear QODD Answer field to empty it from any previous data
            qoddAnswer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

            # Enter answer
            qoddAnswer.send_keys(answer)

            # Submit Form
            submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()
        driver.quit()
            
    else:
        print("Error:", response.status_code, response.text)



