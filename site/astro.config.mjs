import { defineConfig } from 'astro/config';

// The same generator and settings as the sibling sites: a fully static build in dist/.
// Nothing is deployed anywhere (2026-11-17). The address is the one John registered.
export default defineConfig({
  site: 'https://beyondthewindow.org',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
});
