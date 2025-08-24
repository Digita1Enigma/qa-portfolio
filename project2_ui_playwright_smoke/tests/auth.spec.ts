import { test, expect } from '@playwright/test';

test('login success → inventory page', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'secret_sauce');
  await page.click('#login-button');
  await expect(page).toHaveURL(/.*inventory\.html/);

  const items = page.locator('.inventory_item');
  const count = await items.count();
  expect(count).toBeGreaterThan(0);   // ← заменили
});

test('login negative → wrong password', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'wrong_password');
  await page.click('#login-button');

  const err = page.locator('[data-test="error"]');
  await expect(err).toBeVisible();
  await expect(err).toContainText('Username and password do not match');
});
