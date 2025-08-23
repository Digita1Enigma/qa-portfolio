import { test, expect } from '@playwright/test';

test('login shows inventory list', async ({ page }) => {
  await page.goto('/');
  await page.getByPlaceholder('Username').fill('standard_user');
  await page.getByPlaceholder('Password').fill('secret_sauce');
  await page.getByRole('button', { name: 'Login' }).click();

  await expect(page).toHaveURL(/.*inventory\.html/);
  const items = page.locator('.inventory_item');
  const count = await items.count();
  expect(count).toBeGreaterThan(0); // Playwright 1.47+ поддерживает >0 через toHaveCount
});
