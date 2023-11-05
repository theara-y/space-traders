### Steps to Migrate Database ###
- `flask db init` Only if migration repository does not exist.
- `flask db --help` Display help information.

1. Apply changes to models.
2. `flask db migrate` Auto-generates a new revision file.
3. `flask db upgrade` Run upgrade.