import { test, expect } from '@playwright/test';
import { login } from './utils';

test.beforeEach(async ({ page }) => {
  await login(page);
});

test('add single product to cart (Sauce Labs Backpack)', async ({ page }) => {
  const item = page.locator('.inventory_item').filter({ hasText: 'Sauce Labs Backpack' });
  await item.getByRole('button', { name: 'Add to cart' }).click();

  const cartLink = page.locator('.shopping_cart_link');
  await expect(cartLink).toBeVisible();
  // бейдж должен показать 1
  await expect(page.locator('.shopping_cart_badge')).toHaveText('1');

  await cartLink.click();
  await expect(page).toHaveURL(/.*cart\.html/);
  await expect(page.locator('.cart_item')).toHaveCount(1);
  await expect(page.locator('.inventory_item_name')).toContainText('Sauce Labs Backpack');
});
