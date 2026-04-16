# Awesome Cloud Computing - Task Runner
# Run tasks with: just <task-name>

# Display all available commands
default:
    @just --list

# Development server
dev:
    @echo "Starting MkDocs development server..."
    @uv run mkdocs serve

# Sync language configurations
sync-langs:
    @echo "Syncing language configurations..."
    @uv run python scripts/sync_languages.py

# Create new language structure
create-lang locale:
    @echo "Creating language structure for {{locale}}..."
    @uv run python scripts/create_language.py {{locale}}

# Clean build artifacts
clean:
    @echo "Cleaning build artifacts..."
    @rm -rf site/
    @echo "Clean complete!"

# Run quality checks with pre-commit
lint:
    @echo "Running quality checks with pre-commit..."
    @uv run pre-commit run --all-files

# Check for broken links
check-links:
    @echo "Checking for broken links with lychee..."
    @if command -v lychee >/dev/null 2>&1; then \
        lychee --verbose --no-progress --accept 200,204,301,302,307,308 README.md 'docs/**/*.md' && echo "All links are valid!"; \
    else \
        echo "lychee not installed. Install with:"; \
        echo "  cargo install lychee"; \
        echo "  Or download from: https://github.com/lycheeverse/lychee/releases"; \
    fi

# Run all quality checks including link checking
check-all: lint check-links
    @echo "All quality checks completed!"

# Install pre-commit hooks
install-hooks:
    @echo "Installing pre-commit hooks..."
    @uv run pre-commit install
    @echo "Pre-commit hooks installed successfully!"
