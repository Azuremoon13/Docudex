# Docudex Documentation — Contributing

This repository hosts the **Docudex MkDocs site**. All changes to the documentation are automatically built and deployed when merged into `main`.  

## Workflow for Contributors

### 1. Fork or Clone

```bash
# Fork the repo on GitHub or clone directly
git clone https://github.com/azuremoon13/docudex.git
cd docudex
```
### 2. Create a Branch
Always work on a separate branch for your changes:

```bash
git checkout -b my-feature
```

### 3. Edit Documentation
Markdown files are in the repository subdirectories - Follow the LACC folder as a example in docs subdirectories

The navigation is defined in mkdocs.yml in root.

You can preview your changes locally:
```bash
mkdocs serve
Then open http://127.0.0.1:8000 in your browser.
```

### 4. Commit Your Changes
```bash
git add .
git commit -m "Add/update documentation for <feature>"
```

5. Push and Open a Merge Request
```bash
git push origin my-feature
```
Open a merge request (MR) on GitHub targeting the main branch.

Include a short description of your changes.

### 6. Automatic Deployment
Once your MR is merged into main, the deployment process is automatic:
```bash
GitHub MR merged
        │
        ▼
  Webhook triggers
        │
        ▼
   MkDocs builds
   into /build dir
        │
        ▼
     Nginx serves
     site over HTTPS
No manual file transfers or server intervention are required.
```

### 7. Tips for Contributors
Use clear, descriptive commit messages.

Check your changes with mkdocs serve before submitting.

Keep your branch up to date with main to avoid merge conflicts.
