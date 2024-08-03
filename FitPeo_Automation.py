import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Opening FitPeo URL - 1
driver = webdriver.Chrome()
driver.get("https://fitpeo.com/")
driver.maximize_window()

actions = ActionChains(driver)

# Navigate to Revenue Calculator page - 2
rc_page = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Revenue Calculator')]"))
)
rc_page.click()

# Scroll to the slider element - 3
slider = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'MuiSlider-root')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", slider)

# Drag the slider to 820 - 4
slider_thumb = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='range']"))
)
slider_thumb.send_keys(Keys.ARROW_RIGHT * 631)
text_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@id=':r0:'])"))
)
assert text_field.get_attribute("value") == "820"

# Selecting CPT codes - 7
CPT_99091 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[1]"))
)
CPT_99091.click()
CPT_99453 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[2]"))
)
CPT_99453.click()
CPT_99454 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[3]"))
)
CPT_99454.click()
CPT_99474 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[8]"))
)
CPT_99474.click()

# Total Recurring Reimbursement in Header - 9
total_reimbursement_header = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//div[@class='MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular css-1lnu3ao'])/p[4]/p"))
)
assert total_reimbursement_header.text == "$110700"

# Change and validate slider value to 560 from text box - 5,6
actions.click(text_field).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
actions.send_keys('560').perform()
assert text_field.get_attribute("value") == "560"

# Total Recurring Reimbursement with 560 - 8
total_reimbursement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//div[@class='MuiBox-root css-m1khva'])/p[2]"))
)
print(total_reimbursement.text)

driver.quit()