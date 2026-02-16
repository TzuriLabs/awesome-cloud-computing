#!/usr/bin/env python3
"""
Sync language configurations from docs/languages.yml to mkdocs.yml
"""

from pathlib import Path
import sys
import yaml
from rich.panel import Panel
from rich.console import Console

console = Console()

# Const
LANG_FILE = Path("docs/languages.yml")
MKDOCS_FILE = Path("mkdocs.yml")


def load_yaml(path: Path):
    if not path.exists():
        print(f"Error: {path} not found")
        sys.exit(1)
    with path.open("r", encoding="utf-8") as f:
        return yaml.load(f, Loader=MkDocsLoader)


def save_yaml(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )


def build_nav_structure(translations: dict):
    def t(key: str) -> str:
        return translations.get(key, key)

    return [
        {t("Home"): "index.md"},
        {
            t("Learning Resources"): [
                {t("Overview"): "learning/index.md"},
                {t("Basic Concepts"): "learning/basic-concepts.md"},
                {t("Books"): "learning/books.md"},
                {t("Tutorials"): "learning/tutorials.md"},
                {t("Certifications"): "learning/certifications.md"},
            ]
        },
        {t("Platforms"): "platforms.md"},
        {
            t("Tools & Software"): [
                {t("Overview"): "tools/index.md"},
                {t("Infrastructure as Code"): "tools/infrastructure-as-code.md"},
                {t("Multi-cloud Management"): "tools/multi-cloud-management.md"},
                {t("Containerization"): "tools/containerization.md"},
                {t("Serverless Frameworks"): "tools/serverless-frameworks.md"},
                {t("Cloud Migration"): "tools/cloud-migration.md"},
                {t("Disaster Recovery"): "tools/disaster-recovery.md"},
                {t("FinOps & Cost Management"): "tools/finops-cost-management.md"},
                {t("Edge Computing"): "tools/edge-computing.md"},
                {t("Monitoring"): "tools/monitoring.md"},
                {t("Logging"): "tools/logging.md"},
            ]
        },
        {
            t("Best Practices"): [
                {t("Overview"): "best-practices/index.md"},
                {t("Cost Optimization"): "best-practices/cost-optimization.md"},
                {
                    t(
                        "Scalability & Performance"
                    ): "best-practices/scalability-performance.md"
                },
            ]
        },
        {
            t("Security"): [
                {t("Overview"): "security/index.md"},
                {t("Identity & Access Management"): "security/iam.md"},
                {t("Threat Detection"): "security/threat-detection.md"},
                {t("Secret Management"): "security/secret-management.md"},
                {t("Compliance & Governance"): "security/compliance-governance.md"},
            ]
        },
        {t("Community"): "community/index.md"},
        {t("Emerging Trends"): "trends/index.md"},
        {t("Contributing"): "contributing.md"},
    ]


def find_plugin(plugins, name):
    for plugin in plugins:
        if isinstance(plugin, dict) and name in plugin:
            return plugin[name]
    return None


def sync_languages():
    langs_cfg = load_yaml(LANG_FILE).get("languages", [])
    if not langs_cfg:
        console.print(
            Panel.fit(
                "No languages defined in docs/languages.yml",
                title="[red]Error[/red]",
                border_style="red",
            )
        )
        sys.exit(1)

    mkdocs = load_yaml(MKDOCS_FILE)

    plugins = mkdocs.setdefault("plugins", [])

    # --- search plugin ---
    search = find_plugin(plugins, "search")
    if search is None:
        search = {}
        plugins.append({"search": search})

    # search["lang"] = [l["locale"] for l in langs_cfg]
    search["lang"] = [lang["locale"] for lang in langs_cfg]

    # --- i18n plugin ---
    i18n = find_plugin(plugins, "i18n")
    if i18n is None:
        i18n = {}
        plugins.append({"i18n": i18n})

    i18n_languages = []

    for lang in langs_cfg:
        entry = {
            "locale": lang["locale"],
            "name": lang["name"],
            "build": lang.get("build", True),
            "nav": build_nav_structure(lang.get("nav_translations", {})),
        }
        if lang.get("default"):
            entry["default"] = True
        i18n_languages.append(entry)

    i18n["languages"] = i18n_languages

    save_yaml(MKDOCS_FILE, mkdocs)

    console.print("[green]mkdocs.yml successfully synced [green]")
    console.print(f"[cyan]Languages: [{', '.join(lang['name'] for lang in langs_cfg)}]")

    for lang in langs_cfg:
        folder = Path("docs") / lang["locale"]
        if not folder.exists():
            print(f"Missing folder: {folder}/")
            console.print("[yellow]Missing folder:[/yellow] docs/{locale}/")


class PythonName:
    def __init__(self, value: str):
        self.value = value


class MkDocsLoader(yaml.FullLoader):
    pass


def python_name_constructor(loader, suffix, node):
    return PythonName(suffix)


def python_name_representer(dumper, data):
    return dumper.represent_scalar(
        f"tag:yaml.org,2002:python/name:{data.value}",
        "",
    )


MkDocsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    python_name_constructor,
)

yaml.add_representer(PythonName, python_name_representer)


def main():
    console.print(
        Panel.fit(
            "Syncing languages...",
            title="Syncing",
            border_style="cyan",
        )
    )
    sync_languages()
    console.print("[green]Done. Run: $ mkdocs serve[/green]")


if __name__ == "__main__":
    main()
