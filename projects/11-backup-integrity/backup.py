"""Copy a folder and write SHA-256 checksums, then verify them later."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.crypto_utils import sha256_file


def files_under(folder: Path) -> list[Path]:
    return [path for path in folder.rglob("*") if path.is_file() and path.name != "CHECKSUMS.json"]


def create(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    checksums = {
        str(path.relative_to(dest)).replace("\\", "/"): sha256_file(path) for path in files_under(dest)
    }
    (dest / "CHECKSUMS.json").write_text(json.dumps(checksums, indent=2) + "\n", encoding="utf-8")
    print(f"copied {len(checksums)} files to {dest}")


def verify(dest: Path) -> None:
    listed = json.loads((dest / "CHECKSUMS.json").read_text(encoding="utf-8"))
    failed = False
    for relative, expected in listed.items():
        path = dest / relative
        if not path.exists() or sha256_file(path) != expected:
            print(f"changed {relative}")
            failed = True
    if failed:
        sys.exit(1)
    print(f"ok {len(listed)} files")


def main() -> None:
    if len(sys.argv) == 4 and sys.argv[1] == "create":
        create(Path(sys.argv[2]), Path(sys.argv[3]))
        return
    if len(sys.argv) == 3 and sys.argv[1] == "verify":
        verify(Path(sys.argv[2]))
        return
    print("usage: python backup.py create SRC DEST")
    print("       python backup.py verify DEST")
    sys.exit(1)


if __name__ == "__main__":
    main()
