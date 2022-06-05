from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "/Users/jwon/lab/paper/crawling/pdf", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
driver = webdriver.Chrome('/Users/jwon/Documents/chromedriver', options=options)

last_page = 5 
for page in range(1, last_page + 1):

    driver.get(f'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?sdate=2021-04-27&edate=2022-04-27&now_page={page}&search_value=&report_type=DW&pagenum=20&search_text=&business_code=')
    driver.implicitly_wait(10)
    
    for i in range(1, 21):
        driver.find_element_by_xpath(f'//*[@id="contents"]/div[2]/table/tbody/tr[{i}]/td[6]/div/a').click()



