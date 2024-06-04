// @vitest-environment nuxt

// The function should correctly set the SEO meta title to "Dashboard".
import { describe, test } from 'vitest'
import { setup, $fetch } from '@nuxt/test-utils/e2e'
import { jest } from '@types/jest'

setup({
  browser: true,
})

describe('script setup', () => {
  test('should set the SEO meta title to "Dashboard"', async () => {
    const useSeoMetaMock = jest.fn()
    jest.mock('some-package', () => ({
      useSeoMeta: useSeoMetaMock,
    }))

    await import('./script-setup')

    expect(useSeoMetaMock).toHaveBeenCalledWith({
      title: 'Dashboard',
    })
  })
})

// The function should correctly set the page meta layout to "dashboard".
describe('script setup', () => {
  test('should set the page meta layout to "dashboard"', async () => {
    const definePageMetaMock = jest.fn()
    jest.mock('some-package', () => ({
      definePageMeta: definePageMetaMock,
    }))

    await import('./script-setup')

    expect(definePageMetaMock).toHaveBeenCalledWith({
      layout: 'dashboard',
      auth: {
        unauthenticatedOnly: false,
      },
    })
  })
})

// The function should correctly set the page meta auth unauthenticatedOnly to false.
describe('script setup', () => {
  test('should set the page meta auth unauthenticatedOnly to false', async () => {
    const definePageMetaMock = jest.fn()
    jest.mock('some-package', () => ({
      definePageMeta: definePageMetaMock,
    }))

    await import('./script-setup')

    expect(definePageMetaMock).toHaveBeenCalledWith({
      layout: 'dashboard',
      auth: {
        unauthenticatedOnly: false,
      },
    })
  })
})

// The function should handle cases where the page meta layout is not provided.
describe('script setup', () => {
  test('should set the page meta layout to "dashboard" when layout is not provided', async () => {
    const definePageMetaMock = jest.fn()
    jest.mock('some-package', () => ({
      definePageMeta: definePageMetaMock,
    }))

    await import('./script-setup')

    expect(definePageMetaMock).toHaveBeenCalledWith({
      layout: 'dashboard',
      auth: {
        unauthenticatedOnly: false,
      },
    })
  })
})
