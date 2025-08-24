import { Page, expect } from '@playwright/test';

export async function login(page: Page, user = 'standard_user', pass = 'secret_sauce') {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', user);
  await page.fill('#password', pass);
  await page.click('#login-button');
  await expect(page).toHaveURL(/.*inventory\.html/);
}
