"""Build the claude.ai upload ZIP for every skill in this repo.

For each skill folder <name>/<name>/SKILL.md it writes <name>/<name>.zip, with the files inside a top-level
folder called <name>/ (claude.ai rejects an upload whose folder name doesn't match the skill name).
Run it after changing any skill, and commit the ZIP with the change:

    python tools/make-zips.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for skill_md in sorted(ROOT.glob("*/*/SKILL.md")):
    skill_dir = skill_md.parent
    name = skill_dir.name
    if skill_dir.parent.name != name:
        continue
    out = skill_dir.parent / f"{name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file():
                z.write(f, f"{name}/{f.relative_to(skill_dir).as_posix()}")
    print("built", out.relative_to(ROOT), [n for n in zipfile.ZipFile(out).namelist()])
