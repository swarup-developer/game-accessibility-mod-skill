"""Read executable architecture and game-layout hints without modifying a game."""

import argparse
import json
import struct
import sys
from pathlib import Path


MACHINES = {0x014C: "x86", 0x8664: "x64", 0xAA64: "arm64"}


def pe_architecture(path):
    """Inspect a PE header; a launcher may differ from the actual game process."""
    try:
        with path.open("rb") as stream:
            header = stream.read(64)
            if len(header) < 64 or header[:2] != b"MZ":
                return {"status": "not_pe"}
            offset = struct.unpack_from("<I", header, 0x3C)[0]
            if offset < 64 or offset + 6 > path.stat().st_size:
                return {"status": "invalid_pe_offset"}
            stream.seek(offset)
            pe = stream.read(6)
            if len(pe) != 6 or pe[:4] != b"PE\0\0":
                return {"status": "invalid_pe_signature"}
            machine = struct.unpack_from("<H", pe, 4)[0]
            return {
                "status": "ok",
                "machine": hex(machine),
                "architecture": MACHINES.get(machine, "unknown_machine"),
            }
    except OSError as exc:
        return {"status": "unreadable", "error": str(exc)}


def inspect_directory(root):
    """Return file evidence and hints, never a loader-compatibility verdict."""
    entries = sorted(root.iterdir(), key=lambda item: item.name.lower())
    executables = [
        {"file": p.name, **pe_architecture(p)}
        for p in entries if p.is_file() and p.suffix.lower() == ".exe"
    ]
    evidence = []

    def record(relative, hint):
        if (root / relative).exists():
            evidence.append({"path": relative, "hint": hint})

    record("UnityPlayer.dll", "Unity player library present")
    record("GameAssembly.dll", "Native game assembly present; investigate IL2CPP")
    record("BepInEx", "BepInEx-named directory present; inspect logs for actual initialization")
    record("MelonLoader", "MelonLoader-named directory present; inspect logs for actual initialization")
    record("renpy", "Ren'Py-named directory present")
    record("data.win", "GameMaker-style data file present")
    record("Content/Paks", "Unreal-style package directory present")
    for item in entries:
        if item.is_dir() and item.name.lower().endswith("_data"):
            record(f"{item.name}/Managed", "Managed directory present; inspect assemblies and logs")
            record(f"{item.name}/il2cpp_data", "IL2CPP data directory present")
        if item.is_file() and item.suffix.lower() == ".pck":
            evidence.append({"path": item.name, "hint": "Godot-style package present"})
    logs = []
    for relative in ("BepInEx/LogOutput.log", "MelonLoader/Latest.log"):
        path = root / relative
        if path.is_file():
            logs.append({"path": relative, "bytes": path.stat().st_size})
    return {
        "game_directory": str(root),
        "executables": executables,
        "layout_evidence": evidence,
        "log_locations": logs,
        "limitations": [
            "Architecture is from the PE machine header; managed AnyCPU and launcher behavior require runtime confirmation.",
            "Layout hints do not prove engine version, runtime target, successful loader initialization, or mod compatibility.",
            "Only root executables and selected layout paths are inspected; nested or custom installs may need targeted follow-up.",
            "No game is launched and no files are written; logs and game content are not read.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        root = args.game_dir.expanduser().resolve(strict=True)
        if not root.is_dir():
            raise ValueError("The game directory must be a folder.")
        report = inspect_directory(root)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
