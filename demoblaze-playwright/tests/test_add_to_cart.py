from utils import login

def test_add_to_cart(page):
    page.goto("https://www.demoblaze.com")
    login(page, "admin", "admin")

    # click Phones
    page.click("a:has-text('Phones')")

    # click Nokia Lumia 1520
    page.click("a:has-text('Nokia lumia 1520')")

    # add to cart
    page.click("a:has-text('Add to cart')")

    # handle alert
    page.on("dialog", lambda dialog: dialog.accept())

    # go to cart
    page.click("#cartur")

    # assertion
    page.wait_for_selector("td:has-text('Nokia lumia 1520')")
