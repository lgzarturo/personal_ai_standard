"""Export the PAIS Skill and its Markdown references as an offline ZIP."""

import argparse
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "adapters/skills/pais/SKILL.md"
REFERENCES = (
    "BOOTSTRAP.md",
    "CORE.md",
    "LANGUAGE.md",
    "WRITING.md",
    "FEEDBACK.md",
    "projects/README.md",
    "projects/codeconductor/PROJECT_RULES.md",
    "projects/microsdd/PROJECT_RULES.md",
)


def offline_text(path: Path) -> str:
    """Preserve project identities while removing remote source locations."""
    content = path.read_text(encoding="utf-8")
    content = re.sub(r"(?m)^- Website: https?://[^\r\n]+\n", "", content)
    content = content.replace("Base URL: https://github.com/", "Repository: GitHub ")
    content = re.sub(r"https://github\.com/([\w.-]+/[\w.-]+)", r"GitHub \1", content)
    if re.search(r"https?://|git@|ssh://", content, re.IGNORECASE):
        raise ValueError(f"Remote URL in {path.relative_to(ROOT)}")
    return content


def package_skill(output: Path, *, claude: bool) -> None:
    prefix = "pais/" if claude else ""
    files = {"SKILL.md": offline_text(SKILL)}
    files.update({f"references/{name}": offline_text(ROOT / name) for name in REFERENCES})
    files["references/LICENSE.txt"] = offline_text(ROOT / "LICENSE")

    with ZipFile(output, mode="x", compression=ZIP_DEFLATED) as archive:
        for name, content in files.items():
            archive.writestr(prefix + name, content)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New ZIP file to create")
    parser.add_argument("--claude", action="store_true", help="Wrap the skill in a pais/ directory")
    args = parser.parse_args()
    try:
        package_skill(args.output, claude=args.claude)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
