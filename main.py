from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import time
import random


def login():
    """执行登录操作并保存 cookies"""
    driver.get('https://world.xiaomawang.com/')
    login_tip_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'loginTip__1ok96'))
    )
    login_tip_button.click()
    username_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.xmloginant-input#username'))
    )
    username_input.send_keys(username)
    password_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.xmloginant-input#pwd'))
    )
    password_input.send_keys(password)
    checkbox = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.xmloginant-checkbox-input'))
    )
    checkbox.click()
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.xmloginant-btn.login-btn.login-btn-login.xmloginant-btn-primary'))
    )
    login_button.click()
    time.sleep(5)
    # 保存 cookies
    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as file:
        import json
        json.dump(cookies, file)

def load_cookies_and_navigate():
    """加载 cookies 并导航到目标页面"""
    driver.get('https://world.xiaomawang.com/')
    with open('cookies.json', 'r') as file:
        import json
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

def send_message(content, project_id):
    """在指定项目页面发送评论"""
    url = f"https://world.xiaomawang.com/w/person/project/all/{project_id}"
    driver.execute_script(f"window.location.href = '{url}'")
    comment_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.input-comment-inner__3Hl94'))
    )
    comment_box.clear()
    comment_box.send_keys(content)
    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.able-btn__1fnto'))
    )
    submit_button.click()


RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

# 打印版权声明和免责声明
print(f"{RED}{BOLD}" + "=" * 50)
print("版权声明：")
print("版权所有 © Snowy Collie，保留所有权利。")
print("-" * 50)
print("免责声明：")
print("本工具仅供学习和交流使用，请勿用于非法用途。")
print("作者不对任何使用过程中产生的问题负责。")
print("-" * 50)
print("温馨提示：")
print("本工具仅在Windows造作系统运行，使用Edge浏览器及其Driver。")
print("请确保已经将正确版本的msedgedriver.exe放置在当前python文件同目录下。")
print("下载Driver：https://developer.microsoft.com/microsoft-edge/tools/webdriver/")
print("=" * 50 + f"{END}")
if input("是否同意上述声明？(y/n)") == "y":
    # 配置 Edge WebDriver 服务
    service = Service(executable_path='./msedgedriver.exe')

    # 初始化 WebDriver
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 10)
    username=input("请输入手机号：")
    password=input("请输入密码：")
    content = input("请输入要发送的消息：")
    method = input("请输入要使用的发送方式（输入r随机，i按顺序）：")
    start_num = int(input("请输入要发送的起始ID："))
    end_num = int(input("请输入要发送的结束ID："))
    if method == "r":
        num = int(input("请输入要发送的次数："))
        # 执行登录（仅需一次）
        login()

        # 加载 cookies 并开始批量操作
        load_cookies_and_navigate()

        for i in range(num):
            try:
                project_id=random.randint(start_num,end_num+1)
                send_message(content, project_id)
                print(f"Successfully sent message for user {project_id}")

            except Exception as e:
                print(f"Failed to send message for user {project_id}: {e}")

        driver.quit()
    elif method == "i":
        # 执行登录（仅需一次）
        login()

        # 加载 cookies 并开始批量操作
        load_cookies_and_navigate()

        for i in range(start_num,end_num+1):
            try:
                project_id=i
                send_message(content, project_id)
                print(f"Successfully sent message for user {project_id}")

            except Exception as e:
                print(f"Failed to send message for user {project_id}: {e}")

        driver.quit()
    else:
        print("输入错误，程序退出。")
else:
    print("用户未同意声明，程序退出。") 