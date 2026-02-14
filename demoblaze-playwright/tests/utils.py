def login(page, user, pwd):
    page.click("#login2")
    page.fill("#loginusername", user)
    page.fill("#loginpassword", pwd)
    page.click("button[onclick='logIn()']")
    page.wait_for_selector("#nameofuser")
