import { test, expect } from '@playwright/test';
import { login } from './utils';

import { test, expect } from '@playwright/test';
import { login } from './utils';

test.beforeEach(async ({ page }) => {
  await login(page);
  // дождёмся, что мы точно на inventory и элементы видны
  await expect(page).toHaveURL(/.*inventory\.html/);
  await expect(page.locator('[data-test="product_sort_container"]')).toBeVisible();
  await expect(page.locator('.inventory_item')).toHaveCountGreaterThan(0 as any).catch(async () => {
    const c = await page.locator('.inventory_item').count();
    expect(c).toBeGreaterThan(0);
  });
});

test('sort by Price (low → high)', async ({ page }) => {
  await page.selectOption('[data-test="product_sort_container"]', 'lohi');

  const prices = page.locator('.inventory_item_price');
  const n = await prices.count();
  const values: number[] = [];
  for (let i = 0; i < n; i++) {
    const txt = await prices.nth(i).innerText(); // "$29.99"
    values.push(parseFloat(txt.replace('$', '')));
  }
  const sorted = [...values].sort((a, b) => a - b);
  expect(values).toEqual(sorted);
});

test('sort by Name (Z → A)', async ({ page }) => {
  await page.selectOption('[data-test="product_sort_container"]', 'za');

  const names = page.locator('.inventory_item_name');
  const n = await names.count();
  const values: string[] = [];
  for (let i = 0; i < n; i++) {
    values.push((await names.nth(i).innerText()).trim());
  }
  const sorted = [...values].sort((a, b) => b.localeCompare(a));
  expect(values).toEqual(sorted);
});

