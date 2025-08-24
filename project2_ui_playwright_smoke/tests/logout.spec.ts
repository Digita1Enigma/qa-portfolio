import { test, expect } from '@playwright/test';
import { login } from './utils';

test('logout via burger menu', async ({ page }) => {
  await login(page);

  await page.click('#react-burger-menu-btn');
  await page.click('#logout_sidebar_link');

  await expect(page).toHaveURL('https://www.saucedemo.com/');
  await expect(page.locator('#login-button')).toBeVisible();
});
