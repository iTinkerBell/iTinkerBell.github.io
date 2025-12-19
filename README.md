# Boost Library Usage Analysis

This repository hosts comprehensive analysis and statistics of Boost C++ Library usage across GitHub repositories, organized by Boost version.

## Repository Structure

```
.
├── index.html              # Version selector (root landing page)
├── v1.90/                  # Boost 1.90 analysis
│   ├── index.html          # Main dashboard
│   ├── bsl_analysis.html   # BSL-1.0 license analysis
│   ├── data_to_release_note.html  # Release notes data
│   ├── dashboard_data.json # Dashboard data
│   └── libraries/          # Individual library detail pages
│       ├── algorithm.html
│       ├── asio.html
│       └── ...
├── v1.91/                  # Boost 1.91 analysis (when available)
│   └── ...
└── _config.yml             # Jekyll configuration
```

## Adding a New Version

When a new Boost version (e.g., 1.91) becomes available:

1. **Create the version directory:**
   ```bash
   mkdir v1.91
   ```

2. **Copy the structure from the previous version:**
   ```bash
   cp -r v1.90/* v1.91/
   ```

3. **Update the files in v1.91/** with new data:
   - Update `index.html` with new statistics
   - Update `bsl_analysis.html` with new BSL-1.0 data
   - Update `data_to_release_note.html` with new release notes
   - Update `dashboard_data.json` with new dashboard data
   - Update all library detail pages in `libraries/` with new data

4. **Update the root `index.html`:**
   - Add a new version card for v1.91
   - Mark it as "Latest" (remove "Latest" from previous version)
   - Update the JavaScript `latestVersion` variable if auto-redirect is enabled

5. **Update version references:**
   - Search and replace version numbers in the new version's files
   - Update any hardcoded version references (e.g., "Latest Version: 1.90.0" → "1.91.0")

## File Organization

- **Root `index.html`**: Landing page with version selector
- **Version directories (`v1.90/`, `v1.91/`, etc.)**: Each contains a complete set of analysis pages for that version
- **Library detail pages**: Located in `v{version}/libraries/` directory

## Navigation

- Users land on the root `index.html` and select a version
- Within each version, navigation links are relative (no version prefix needed)
- Library pages link back to their version's dashboard using `../index.html`
- All version pages include a "Back to Version Selector" link

## Notes

- All internal links within a version directory use relative paths
- The root index.html uses absolute paths with version prefixes (e.g., `v1.90/index.html`)
- When adding new versions, ensure all links are updated correctly

