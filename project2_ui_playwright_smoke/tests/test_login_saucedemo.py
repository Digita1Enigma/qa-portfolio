def test_login_inventory(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")
    assert "inventory" in page.url
    # Проверим, что есть хотя бы один товар
    items = page.locator(".inventory_item")
    assert items.count() > 0
